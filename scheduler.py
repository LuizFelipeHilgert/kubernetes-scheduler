import random

workers = {
    "trabalho-worker": {
        "cpu": 8,
        "ram": 16,
        "disk": 100
    },
    "trabalho-worker2": {
        "cpu": 4,
        "ram": 8,
        "disk": 200
    }
}

pods = [
    {"name": "pod1", "cpu": 1, "ram": 1, "disk": 10},
    {"name": "pod2", "cpu": 2, "ram": 2, "disk": 20},
    {"name": "pod3", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod4", "cpu": 3, "ram": 4, "disk": 30},
    {"name": "pod5", "cpu": 2, "ram": 1, "disk": 15},
    {"name": "pod6", "cpu": 1, "ram": 2, "disk": 10},
    {"name": "pod7", "cpu": 2, "ram": 3, "disk": 25},
    {"name": "pod8", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod9", "cpu": 2, "ram": 2, "disk": 10},
    {"name": "pod10", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod11", "cpu": 2, "ram": 4, "disk": 40},
    {"name": "pod12", "cpu": 1, "ram": 2, "disk": 15},
]

def choose_worker(pod):
    best_worker = None
    best_score = -1

    for name, resources in workers.items():

        if (
            resources["cpu"] >= pod["cpu"] and
            resources["ram"] >= pod["ram"] and
            resources["disk"] >= pod["disk"]
        ):

            score = (
                resources["cpu"] +
                resources["ram"] +
                resources["disk"]
            )

            if score > best_score:
                best_score = score
                best_worker = name

    return best_worker

for pod in pods:

    worker = choose_worker(pod)

    if worker:
        workers[worker]["cpu"] -= pod["cpu"]
        workers[worker]["ram"] -= pod["ram"]
        workers[worker]["disk"] -= pod["disk"]

import random

workers = {
    "trabalho-worker": {
        "cpu": 8,
        "ram": 16,
        "disk": 100
    },
    "trabalho-worker2": {
        "cpu": 4,
        "ram": 8,
        "disk": 200
    }
}

pods = [
    {"name": "pod1", "cpu": 1, "ram": 1, "disk": 10},
    {"name": "pod2", "cpu": 2, "ram": 2, "disk": 20},
    {"name": "pod3", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod4", "cpu": 3, "ram": 4, "disk": 30},
    {"name": "pod5", "cpu": 2, "ram": 1, "disk": 15},
    {"name": "pod6", "cpu": 1, "ram": 2, "disk": 10},
    {"name": "pod7", "cpu": 2, "ram": 3, "disk": 25},
    {"name": "pod8", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod9", "cpu": 2, "ram": 2, "disk": 10},
    {"name": "pod10", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod11", "cpu": 2, "ram": 4, "disk": 40},
    {"name": "pod12", "cpu": 1, "ram": 2, "disk": 15},
]

def choose_worker(pod):
    best_worker = None
    best_score = -1

    for name, resources in workers.items():

        if (
            resources["cpu"] >= pod["cpu"] and
            resources["ram"] >= pod["ram"] and
            resources["disk"] >= pod["disk"]
        ):

            score = (
                resources["cpu"] +
                resources["ram"] +
                resources["disk"]
            )

            if score > best_score:
                best_score = score
                best_worker = name

    return best_worker

for pod in pods:

    worker = choose_worker(pod)

    if worker:
        workers[worker]["cpu"] -= pod["cpu"]
        workers[worker]["ram"] -= pod["ram"]
        workers[worker]["disk"] -= pod["disk"]

import random

workers = {
    "trabalho-worker": {
        "cpu": 8,
        "ram": 16,
        "disk": 100
    },
    "trabalho-worker2": {
        "cpu": 4,
        "ram": 8,
        "disk": 200
    }
}

pods = [
    {"name": "pod1", "cpu": 1, "ram": 1, "disk": 10},
    {"name": "pod2", "cpu": 2, "ram": 2, "disk": 20},
    {"name": "pod3", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod4", "cpu": 3, "ram": 4, "disk": 30},
    {"name": "pod5", "cpu": 2, "ram": 1, "disk": 15},
    {"name": "pod6", "cpu": 1, "ram": 2, "disk": 10},
    {"name": "pod7", "cpu": 2, "ram": 3, "disk": 25},
    {"name": "pod8", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod9", "cpu": 2, "ram": 2, "disk": 10},
    {"name": "pod10", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod11", "cpu": 2, "ram": 4, "disk": 40},
    {"name": "pod12", "cpu": 1, "ram": 2, "disk": 15},
]

def choose_worker(pod):
    best_worker = None
    best_score = -1

    for name, resources in workers.items():

        if (
            resources["cpu"] >= pod["cpu"] and
            resources["ram"] >= pod["ram"] and
            resources["disk"] >= pod["disk"]
        ):

            score = (
                resources["cpu"] +
                resources["ram"] +
                resources["disk"]
            )

            if score > best_score:
                best_score = score
                best_worker = name

    return best_worker

for pod in pods:

    worker = choose_worker(pod)

    if worker:
        workers[worker]["cpu"] -= pod["cpu"]
        workers[worker]["ram"] -= pod["ram"]
        workers[worker]["disk"] -= pod["disk"]

import random

workers = {
    "trabalho-worker": {
        "cpu": 8,
        "ram": 16,
        "disk": 100
    },
    "trabalho-worker2": {
        "cpu": 4,
        "ram": 8,
        "disk": 200
    }
}

pods = [
    {"name": "pod1", "cpu": 1, "ram": 1, "disk": 10},
    {"name": "pod2", "cpu": 2, "ram": 2, "disk": 20},
    {"name": "pod3", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod4", "cpu": 3, "ram": 4, "disk": 30},
    {"name": "pod5", "cpu": 2, "ram": 1, "disk": 15},
    {"name": "pod6", "cpu": 1, "ram": 2, "disk": 10},
    {"name": "pod7", "cpu": 2, "ram": 3, "disk": 25},
    {"name": "pod8", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod9", "cpu": 2, "ram": 2, "disk": 10},
    {"name": "pod10", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod11", "cpu": 2, "ram": 4, "disk": 40},
    {"name": "pod12", "cpu": 1, "ram": 2, "disk": 15},
]

def choose_worker(pod):
    best_worker = None
    best_score = -1

    for name, resources in workers.items():

        if (
            resources["cpu"] >= pod["cpu"] and
            resources["ram"] >= pod["ram"] and
            resources["disk"] >= pod["disk"]
        ):

            score = (
                resources["cpu"] +
                resources["ram"] +
                resources["disk"]
            )

            if score > best_score:
                best_score = score
                best_worker = name

    return best_worker

for pod in pods:

    worker = choose_worker(pod)

    if worker:
        workers[worker]["cpu"] -= pod["cpu"]
        workers[worker]["ram"] -= pod["ram"]
        workers[worker]["disk"] -= pod["disk"]

import random

workers = {
    "trabalho-worker": {
        "cpu": 8,
        "ram": 16,
        "disk": 100
    },
    "trabalho-worker2": {
        "cpu": 4,
        "ram": 8,
        "disk": 200
    }
}

pods = [
    {"name": "pod1", "cpu": 1, "ram": 1, "disk": 10},
    {"name": "pod2", "cpu": 2, "ram": 2, "disk": 20},
    {"name": "pod3", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod4", "cpu": 3, "ram": 4, "disk": 30},
    {"name": "pod5", "cpu": 2, "ram": 1, "disk": 15},
    {"name": "pod6", "cpu": 1, "ram": 2, "disk": 10},
    {"name": "pod7", "cpu": 2, "ram": 3, "disk": 25},
    {"name": "pod8", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod9", "cpu": 2, "ram": 2, "disk": 10},
    {"name": "pod10", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod11", "cpu": 2, "ram": 4, "disk": 40},
    {"name": "pod12", "cpu": 1, "ram": 2, "disk": 15},
]

def choose_worker(pod):
    best_worker = None
    best_score = -1

    for name, resources in workers.items():

        if (
            resources["cpu"] >= pod["cpu"] and
            resources["ram"] >= pod["ram"] and
            resources["disk"] >= pod["disk"]
        ):

            score = (
                resources["cpu"] +
                resources["ram"] +
                resources["disk"]
            )

            if score > best_score:
                best_score = score
                best_worker = name

    return best_worker

for pod in pods:

    worker = choose_worker(pod)

    if worker:
        workers[worker]["cpu"] -= pod["cpu"]
        workers[worker]["ram"] -= pod["ram"]
        workers[worker]["disk"] -= pod["disk"]

import random

workers = {
    "trabalho-worker": {
        "cpu": 8,
        "ram": 16,
        "disk": 100
    },
    "trabalho-worker2": {
        "cpu": 4,
        "ram": 8,
        "disk": 200
    }
}

pods = [
    {"name": "pod1", "cpu": 1, "ram": 1, "disk": 10},
    {"name": "pod2", "cpu": 2, "ram": 2, "disk": 20},
    {"name": "pod3", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod4", "cpu": 3, "ram": 4, "disk": 30},
    {"name": "pod5", "cpu": 2, "ram": 1, "disk": 15},
    {"name": "pod6", "cpu": 1, "ram": 2, "disk": 10},
    {"name": "pod7", "cpu": 2, "ram": 3, "disk": 25},
    {"name": "pod8", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod9", "cpu": 2, "ram": 2, "disk": 10},
    {"name": "pod10", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod11", "cpu": 2, "ram": 4, "disk": 40},
    {"name": "pod12", "cpu": 1, "ram": 2, "disk": 15},
]

def choose_worker(pod):
    best_worker = None
    best_score = -1

    for name, resources in workers.items():

        if (
            resources["cpu"] >= pod["cpu"] and
            resources["ram"] >= pod["ram"] and
            resources["disk"] >= pod["disk"]
        ):

            score = (
                resources["cpu"] +
                resources["ram"] +
                resources["disk"]
            )

            if score > best_score:
                best_score = score
                best_worker = name

    return best_worker

for pod in pods:

    worker = choose_worker(pod)

    if worker:
        workers[worker]["cpu"] -= pod["cpu"]
        workers[worker]["ram"] -= pod["ram"]
        workers[worker]["disk"] -= pod["disk"]

import random

workers = {
    "trabalho-worker": {
        "cpu": 8,
        "ram": 16,
        "disk": 100
    },
    "trabalho-worker2": {
        "cpu": 4,
        "ram": 8,
        "disk": 200
    }
}

pods = [
    {"name": "pod1", "cpu": 1, "ram": 1, "disk": 10},
    {"name": "pod2", "cpu": 2, "ram": 2, "disk": 20},
    {"name": "pod3", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod4", "cpu": 3, "ram": 4, "disk": 30},
    {"name": "pod5", "cpu": 2, "ram": 1, "disk": 15},
    {"name": "pod6", "cpu": 1, "ram": 2, "disk": 10},
    {"name": "pod7", "cpu": 2, "ram": 3, "disk": 25},
    {"name": "pod8", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod9", "cpu": 2, "ram": 2, "disk": 10},
    {"name": "pod10", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod11", "cpu": 2, "ram": 4, "disk": 40},
    {"name": "pod12", "cpu": 1, "ram": 2, "disk": 15},
]

def choose_worker(pod):
    best_worker = None
    best_score = -1

    for name, resources in workers.items():

        if (
            resources["cpu"] >= pod["cpu"] and
            resources["ram"] >= pod["ram"] and
            resources["disk"] >= pod["disk"]
        ):

            score = (
                resources["cpu"] +
                resources["ram"] +
                resources["disk"]
            )

            if score > best_score:
                best_score = score
                best_worker = name

    return best_worker

for pod in pods:

    worker = choose_worker(pod)

    if worker:
        workers[worker]["cpu"] -= pod["cpu"]
        workers[worker]["ram"] -= pod["ram"]
        workers[worker]["disk"] -= pod["disk"]

import random

workers = {
    "trabalho-worker": {
        "cpu": 8,
        "ram": 16,
        "disk": 100
    },
    "trabalho-worker2": {
        "cpu": 4,
        "ram": 8,
        "disk": 200
    }
}

pods = [
    {"name": "pod1", "cpu": 1, "ram": 1, "disk": 10},
    {"name": "pod2", "cpu": 2, "ram": 2, "disk": 20},
    {"name": "pod3", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod4", "cpu": 3, "ram": 4, "disk": 30},
    {"name": "pod5", "cpu": 2, "ram": 1, "disk": 15},
    {"name": "pod6", "cpu": 1, "ram": 2, "disk": 10},
    {"name": "pod7", "cpu": 2, "ram": 3, "disk": 25},
    {"name": "pod8", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod9", "cpu": 2, "ram": 2, "disk": 10},
    {"name": "pod10", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod11", "cpu": 2, "ram": 4, "disk": 40},
    {"name": "pod12", "cpu": 1, "ram": 2, "disk": 15},
]

def choose_worker(pod):
    best_worker = None
    best_score = -1

    for name, resources in workers.items():

        if (
            resources["cpu"] >= pod["cpu"] and
            resources["ram"] >= pod["ram"] and
            resources["disk"] >= pod["disk"]
        ):

            score = (
                resources["cpu"] +
                resources["ram"] +
                resources["disk"]
            )

            if score > best_score:
                best_score = score
                best_worker = name

    return best_worker

for pod in pods:

    worker = choose_worker(pod)

    if worker:
        workers[worker]["cpu"] -= pod["cpu"]
        workers[worker]["ram"] -= pod["ram"]
        workers[worker]["disk"] -= pod["disk"]

import random

workers = {
    "kind-worker": {
        "cpu": 8,
        "ram": 16,
        "disk": 100
    },
    "kind-worker2": {
        "cpu": 4,
        "ram": 8,
        "disk": 200
    }
}

pods = [
    {"name": "pod1", "cpu": 1, "ram": 1, "disk": 10},
    {"name": "pod2", "cpu": 2, "ram": 2, "disk": 20},
    {"name": "pod3", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod4", "cpu": 3, "ram": 4, "disk": 30},
    {"name": "pod5", "cpu": 2, "ram": 1, "disk": 15},
    {"name": "pod6", "cpu": 1, "ram": 2, "disk": 10},
    {"name": "pod7", "cpu": 2, "ram": 3, "disk": 25},
    {"name": "pod8", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod9", "cpu": 2, "ram": 2, "disk": 10},
    {"name": "pod10", "cpu": 1, "ram": 1, "disk": 5},
    {"name": "pod11", "cpu": 2, "ram": 4, "disk": 40},
    {"name": "pod12", "cpu": 1, "ram": 2, "disk": 15},
]

def choose_worker(pod):

    best_worker = None
    best_score = -1

    for name, resources in workers.items():

        if (
            resources["cpu"] >= pod["cpu"] and
            resources["ram"] >= pod["ram"] and
            resources["disk"] >= pod["disk"]
        ):

            score = (
                resources["cpu"] +
                resources["ram"] +
                resources["disk"]
            )

            if score > best_score:
                best_score = score
                best_worker = name

    return best_worker

for pod in pods:

    worker = choose_worker(pod)

    if worker:

        workers[worker]["cpu"] -= pod["cpu"]
        workers[worker]["ram"] -= pod["ram"]
        workers[worker]["disk"] -= pod["disk"]

        print(f"{pod['name']} -> {worker}")

        yaml = f'''
apiVersion: v1
kind: Pod
metadata:
  name: {pod['name']}

spec:
  nodeSelector:
    kubernetes.io/hostname: {worker}

  containers:
  - name: nginx
    image: nginx
'''

        with open(f"pods/{pod['name']}.yaml", "w") as f:
            f.write(yaml)

    else:
        print(f"{pod['name']} -> SEM RECURSOS")

print("\nRECURSOS FINAIS\n")

for worker, resources in workers.items():
    print(worker, resources)
