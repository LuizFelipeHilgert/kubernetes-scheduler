import os

WORKERS = {
    "kind-worker": {
        "cpu": 8,
        "ram": 16,
        "disk": 100,
    },
    "kind-worker2": {
        "cpu": 4,
        "ram": 8,
        "disk": 200,
    },
}

PODS = [
    {"name": "pod1",  "cpu": 1, "ram": 1, "disk": 10},
    {"name": "pod2",  "cpu": 2, "ram": 2, "disk": 20},
    {"name": "pod3",  "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod4",  "cpu": 3, "ram": 4, "disk": 30},
    {"name": "pod5",  "cpu": 2, "ram": 1, "disk": 15},
    {"name": "pod6",  "cpu": 1, "ram": 2, "disk": 10},
    {"name": "pod7",  "cpu": 2, "ram": 3, "disk": 25},
    {"name": "pod8",  "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod9",  "cpu": 2, "ram": 2, "disk": 10},
    {"name": "pod10", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod11", "cpu": 2, "ram": 4, "disk": 40},
    {"name": "pod12", "cpu": 1, "ram": 2, "disk": 15},
]

# Capacidade inicial de cada worker, usada para normalizar o score.
INITIAL_CAPACITY = {name: dict(res) for name, res in WORKERS.items()}

# Estado mutável dos workers (recursos disponíveis).
available = {name: dict(res) for name, res in WORKERS.items()}


def choose_worker(pod: dict) -> str | None:
    """
    Escolhe o worker com mais recursos disponíveis (most-available).

    O score é calculado como a média dos recursos disponíveis normalizados
    pela capacidade inicial, evitando que o disco domine por ter valores
    absolutos maiores.

    Retorna o nome do worker escolhido, ou None se nenhum tiver recursos
    suficientes para o pod.
    """
    best_worker = None
    best_score = -1.0

    for name, resources in available.items():
        fits = (
            resources["cpu"]  >= pod["cpu"]  and
            resources["ram"]  >= pod["ram"]  and
            resources["disk"] >= pod["disk"]
        )
        if not fits:
            continue

        capacity = INITIAL_CAPACITY[name]
        score = (
            resources["cpu"]  / capacity["cpu"]  +
            resources["ram"]  / capacity["ram"]  +
            resources["disk"] / capacity["disk"]
        ) / 3

        if score > best_score:
            best_score = score
            best_worker = name

    return best_worker


def generate_yaml(pod_name: str, worker: str) -> str:
    return f"""\
apiVersion: v1
kind: Pod
metadata:
  name: {pod_name}
spec:
  nodeSelector:
    kubernetes.io/hostname: {worker}
  containers:
  - name: nginx
    image: nginx
"""


def main() -> None:
    os.makedirs("pods", exist_ok=True)

    unscheduled = []

    for pod in PODS:
        worker = choose_worker(pod)

        if worker:
            available[worker]["cpu"]  -= pod["cpu"]
            available[worker]["ram"]  -= pod["ram"]
            available[worker]["disk"] -= pod["disk"]

            print(f"{pod['name']} -> {worker}")

            yaml_content = generate_yaml(pod["name"], worker)
            with open(f"pods/{pod['name']}.yaml", "w") as f:
                f.write(yaml_content)
        else:
            print(f"{pod['name']} -> SEM RECURSOS")
            unscheduled.append(pod)

    print("\n--- RECURSOS FINAIS ---\n")
    for name, resources in available.items():
        print(f"{name}: {resources}")

    if unscheduled:
        print(f"\n--- PODS NÃO AGENDADOS ({len(unscheduled)}) ---\n")
        for pod in unscheduled:
            print(f"  {pod['name']} (cpu={pod['cpu']}, ram={pod['ram']}, disk={pod['disk']})")


if __name__ == "__main__":
    main()
