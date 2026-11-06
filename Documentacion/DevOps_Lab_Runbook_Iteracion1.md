# DevOps Lab - Documentación Operativa
## Iteración 1

### Objetivo
Mantener una referencia rápida del estado actual de la VM, componentes instalados, ubicaciones, comandos operativos y procedimientos de recuperación.

## Usuario Principal
- Usuario: `devops`
- Home: `/home/devops`

## Repositorio Git
**Remoto**
```bash
git@github.com:Budita98/devops-lab.git
```

**Local**
```bash
/home/devops/devops-lab
```

Verificar:
```bash
git remote -v
```

## Docker y Docker Compose
Ver contenedores:
```bash
docker ps
```

Reconstruir stack:
```bash
cd ~/devops-lab
docker compose up -d --build
```

Detener stack:
```bash
docker compose down
```

## Aplicación
Arquitectura:

Browser -> Nginx -> Flask

URL principal:
```text
http://IP_VM:8080
```

## Observabilidad
Prometheus:
```text
http://IP_VM:9090
```

Grafana:
```text
http://IP_VM:3000
```

cAdvisor:
```text
http://IP_VM:8081
```

Node Exporter:
```text
http://IP_VM:9100/metrics
```

## GitHub Actions
Workflow:
```text
.github/workflows/deploy.yml
```

## Self Hosted Runner
Ubicación:
```text
/home/devops/actions-runner
```

Iniciar:
```bash
cd ~/actions-runner
./run.sh
```

## Ansible
Ubicación:
```text
/home/devops/devops-lab/ansible
```

Deploy:
```bash
ansible-playbook -i inventory.ini deploy.yml
```

## Kubernetes
Iniciar cluster:
```bash
minikube start --driver=docker
```

Ver pods:
```bash
kubectl get pods
```

Ver servicios:
```bash
kubectl get svc
```

## Problemas Conocidos
### Hora incorrecta
```bash
chronyc tracking
sudo chronyc makestep
```

### Runner en Queue
Verificar que actions-runner esté ejecutándose.

### Kubernetes no responde
```bash
minikube start --driver=docker
```

## Estado Final Iteración 1
- Linux y SSH Hardening
- Git y GitHub
- Docker y Docker Compose
- Flask
- Nginx Reverse Proxy
- Prometheus
- Grafana
- cAdvisor
- GitHub Actions
- Self Hosted Runner
- Ansible
- Kubernetes Básico
