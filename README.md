# Kubernetes Scheduler

Projeto acadêmico desenvolvido para estudar conceitos de escalonamento distribuído utilizando Kubernetes, Python e Docker.

O projeto implementa um scheduler customizado capaz de consultar recursos disponíveis nos nós do cluster e distribuir cargas de trabalho entre os workers de acordo com a disponibilidade de recursos.

---

# Objetivo

O objetivo deste projeto é simular o funcionamento de um scheduler distribuído em um cluster Kubernetes.

O scheduler:

- Detecta automaticamente os workers do cluster Kubernetes.
- Consulta métricas reais de CPU dos nós.
- Consulta métricas reais de memória RAM dos nós.
- Utiliza armazenamento (disco) modelado na aplicação.
- Calcula a capacidade disponível de cada worker.
- Distribui pods entre os workers de acordo com os recursos disponíveis.
- Identifica pods que não podem ser agendados por falta de recursos.
- Gera automaticamente os manifestos YAML dos pods.

Toda a execução ocorre em um cluster Kubernetes local criado com Kind.

---

# Tecnologias Utilizadas

- Python 3
- Kubernetes
- Kind
- Docker Desktop
- Metrics Server
- kubectl

---

# Estrutura do Cluster

O cluster foi criado utilizando Kind e possui:

- 1 Control Plane
- 2 Worker Nodes

---

# Algoritmo de Escalonamento

O scheduler consulta os workers disponíveis através do comando:

```bash
kubectl get nodes
```

Em seguida, obtém métricas reais de CPU e memória através do Metrics Server:

```bash
kubectl top nodes
```

Para cada pod é calculado um score baseado na disponibilidade dos recursos do worker.

O worker com maior capacidade relativa disponível é escolhido para receber o pod.

Caso nenhum worker possua recursos suficientes, o pod é marcado como não agendado.

---

# Execução do Projeto

## 1. Criar o Cluster

```bash
kind create cluster --config config.yaml
```

---

## 2. Verificar os Nós

```bash
kubectl get nodes
```

### Resultado

![Nodes](./screenshots/kubectl-get-nodes.png)

---

## 3. Verificar os Pods do Cluster

```bash
kubectl get pods -A
```

### Resultado

![Pods](./screenshots/kubectl-get-pods.png)

---

## 4. Verificar Métricas dos Nós

```bash
kubectl top nodes
```

### Resultado

![Top Nodes](./screenshots/kubectl-top-nodes.png)

---

## 5. Executar o Scheduler

```bash
python3 scheduler.py
```

O scheduler:

- Detecta os workers.
- Consulta métricas reais de CPU e memória.
- Realiza o escalonamento.
- Gera automaticamente os arquivos YAML dos pods.

### Resultado

![Scheduler](./screenshots/scheduler-output.png)

---

## 6. Aplicar os Pods no Cluster

```bash
kubectl apply -f pods/
```

---

## 7. Verificar Distribuição dos Pods

```bash
kubectl get pods -o wide
```

---

# Docker Desktop

O cluster Kubernetes criado pelo Kind é executado dentro de containers Docker.

Containers utilizados:

- kind-control-plane
- kind-worker
- kind-worker2

### Resultado

![Docker Cluster](./screenshots/docker-cluster.png)

---

# Métricas dos Containers

## Control Plane

![Control Plane](./screenshots/control-plane-stats.png)

---

## Worker 1

![Worker 1](./screenshots/worker1-stats.png)

---

## Worker 2

![Worker 2](./screenshots/worker2-stats.png)

---

# Estrutura do Projeto

```text
.
├── config.yaml
├── scheduler.py
├── README.md
├── pods/
│   ├── pod1.yaml
│   ├── pod2.yaml
│   └── ...
└── screenshots/
```

---

# Observações

- CPU e memória são obtidas em tempo real através do Metrics Server.
- O armazenamento é modelado na aplicação para fins de simulação.

