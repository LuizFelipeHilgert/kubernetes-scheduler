import os
import subprocess


def get_workers():

    workers = {}

    nodes_output = subprocess.check_output(
        ["kubectl", "get", "nodes", "-o", "name"],
        text=True
    )

    top_output = subprocess.check_output(
        ["kubectl", "top", "nodes", "--no-headers"],
        text=True
    )

    metrics = {}

    for line in top_output.splitlines():

        parts = line.split()

        node_name = parts[0]

        cpu_usage = parts[1]
        memory_usage = parts[3]

        cpu_used = int(cpu_usage.replace("m", ""))

        if memory_usage.endswith("Mi"):
            ram_used = int(memory_usage.replace("Mi", ""))
        elif memory_usage.endswith("Gi"):
            ram_used = int(
                float(memory_usage.replace("Gi", "")) * 1024
            )
        else:
            ram_used = 0

        metrics[node_name] = {
            "cpu_used": cpu_used,
            "ram_used": ram_used
        }

    for line in nodes_output.splitlines():

        node_name = line.replace("node/", "")

        if "control-plane" in node_name:
            continue

        cpu_used = metrics.get(
            node_name,
            {}
        ).get("cpu_used", 0)

        ram_used = metrics.get(
            node_name,
            {}
        ).get("ram_used", 0)

        workers[node_name] = {
            "cpu": max(1, 4000 - cpu_used),
            "ram": max(1, 8192 - ram_used),
            "disk": 100
        }

    return workers


WORKERS = get_workers()

PODS = [
    {"name": "pod1", "cpu": 100, "ram": 100, "disk": 10},
    {"name": "pod2", "cpu": 200, "ram": 200, "disk": 20},
    {"name": "pod3", "cpu": 100, "ram": 100, "disk": 5},
    {"name": "pod4", "cpu": 300, "ram": 400, "disk": 30},
    {"name": "pod5", "cpu": 200, "ram": 100, "disk": 15},
    {"name": "pod6", "cpu": 100, "ram": 200, "disk": 10},
    {"name": "pod7", "cpu": 200, "ram": 300, "disk": 25},
    {"name": "pod8", "cpu": 100, "ram": 100, "disk": 5},
    {"name": "pod9", "cpu": 200, "ram": 200, "disk": 10},
    {"name": "pod10", "cpu": 100, "ram": 100, "disk": 5},
    {"name": "pod11", "cpu": 200, "ram": 400, "disk": 40},
    {"name": "pod12", "cpu": 100, "ram": 200, "disk": 15},
]

INITIAL_CAPACITY = {
    name: dict(res)
    for name, res in WORKERS.items()
}

available = {
    name: dict(res)
    for name, res in WORKERS.items()
}


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

    for worker, resources in WORKERS.items():
        print(f"{worker}: {resources}")

    print("\nESCALONAMENTO\n")

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
        print(f"{name}: {resources}")

    if unscheduled:

        print(
            f"\nPODS NÃO AGENDADOS ({len(unscheduled)}) \n"
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
