# Kubernetes Custom Scheduler

Projeto desenvolvido para a disciplina de Laboratório de Sistemas Operacionais.

## Objetivo

Desenvolver um scheduler customizado para Kubernetes capaz de distribuir pods entre nós workers utilizando múltiplas métricas de recursos.

## Cluster utilizado

O cluster foi criado com Kind contendo:

* 1 control-plane
* 2 worker nodes

Estrutura:

* kind-control-plane
* kind-worker
* kind-worker2

## Métricas utilizadas no escalonamento

O scheduler desenvolvido considera:

* CPU disponível
* Memória RAM disponível
* Espaço em disco disponível

## Funcionamento

O `scheduler.py`:

* lê os recursos disponíveis de cada worker
* compara com os requisitos dos pods
* escolhe o nó com melhor capacidade disponível
* gera automaticamente os arquivos YAML
* aplica os pods no cluster

## Resultado obtido

Distribuição dos pods:

* pod1 → kind-worker2
* pod2 → kind-worker2
* pod3 → kind-worker2
* pod4 → kind-worker
* pod5 → kind-worker
* pod6 → kind-worker
* pod7 → kind-worker

Pods restantes:

* pod8 → sem recursos
* pod9 → sem recursos
* pod10 → sem recursos
* pod11 → sem recursos
* pod12 → sem recursos

## Comandos utilizados

Criar cluster:

```bash
kind create cluster --config config.yaml
```

Executar scheduler:

```bash
python3 scheduler.py
```

Aplicar pods:

```bash
kubectl apply -f pods/
```

Verificar nós:

```bash
kubectl get nodes
```

Verificar pods:

```bash
kubectl get pods -o wide
```

## Tecnologias utilizadas

* Python 3
* Kubernetes
* Kind
* Docker Desktop
* kubectl
* Git / GitHub

## Autor

Luiz Felipe Hilgert

