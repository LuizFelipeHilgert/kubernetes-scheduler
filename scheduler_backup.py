import os
import subprocess


def get_workers():
    result = subprocess.check_output(
        ["kubectl", "get", "nodes", "-o", "name"],
        text=True
    )

    workers = {}

    for line in result.splitlines():
        node_name = line.replace("node/", "")

        if "control-plane" not in node_name:
            workers[node_name] = {
                "cpu": 8,
                "ram": 16,
                "disk": 100
            }

    return workers


WORKERS = get_workers()

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

INITIAL_CAPACITY = {name: dict(res) for name, res in WORKERS.items()}
available = {name: dict(res) for name, res in WORKERS.items()}


def choose_worker(pod):
    best_worker = None
    best_score = -1

    for name, resources in available.items():

        fits = (
            resources["cpu"] >= pod["cpu"]
            and resources["ram"] >= pod["ram"]
            and resources["disk"] >= pod["disk"]
        )

        if not fits:
            continue

        capacity = INITIAL_CAPACITY[name]

        score = (
            resources["cpu"] / capacity["cpu"]
            + resources["ram"] / capacity["ram"]
            + resources["disk"] / capacity["disk"]
        ) / 3

        if score > best_score:
            best_score = score
            best_worker = name

    return best_worker


def generate_yaml(pod_name, worker):
    return f"""apiVersion: v1
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


def main():

    os.makedirs("pods", exist_ok=True)

    print("\nWORKERS DETECTADOS NO CLUSTER:\n")

    for worker in WORKERS:
        print(worker)

    print("\nINICIANDO ESCALONAMENTO...\n")

    unscheduled = []

    for pod in PODS:

        worker = choose_worker(pod)

        if worker:

            available[worker]["cpu"] -= pod["cpu"]
            available[worker]["ram"] -= pod["ram"]
            available[worker]["disk"] -= pod["disk"]

            print(f"{pod['name']} -> {worker}")

            yaml_content = generate_yaml(
                pod["name"],
                worker
            )

            with open(
                f"pods/{pod['name']}.yaml",
                "w"
            ) as f:
                f.write(yaml_content)

        else:

            print(
                f"{pod['name']} -> SEM RECURSOS"
            )

            unscheduled.append(pod)

    print("\nRECURSOS FINAIS\n")

    for name, resources in available.items():
        print(name, resources)

    if unscheduled:

        print(
            f"\nPODS NÃO AGENDADOS ({len(unscheduled)})\n"
        )

        for pod in unscheduled:
            print(
                f"{pod['name']} "
                f"(cpu={pod['cpu']}, "
                f"ram={pod['ram']}, "
                f"disk={pod['disk']})"
            )


if __name__ == "__main__":
    main()
