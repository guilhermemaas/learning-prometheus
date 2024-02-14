#Install:
# for ARM systems, set ARCH to: `arm64`, `armv6` or `armv7`
ARCH=amd64
PLATFORM=$(uname -s)_$ARCH

curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"

# (Optional) Verify checksum
curl -sL "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt" | grep $PLATFORM | sha256sum --check

tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz

sudo mv /tmp/eksctl /usr/local/bin

#Criar Cluster:
eksctl create cluster --name=gmaas-cluster --version=1.23 --region=us-east-1 --nodegroup-name=linuxtips-nodegroup --node-type=t3.medium --nodes=2 --nodes-min=1 --nodes-max=3 --managed

#Comandos eksctl e aws eks:

#Detalhar cluster
aws eks describe-cluster --name=gmaas-cluster

#Atualizar nodegroup:
aws eks update-nodegroup-version --cluster-name=gmaas-cluster --nodegroup-name=linuxtips-nodegroup

#Listar nodegroup:
aws eks describe-nodegroup --cluster-name=gmaas-cluster --nodegroup=linuxtips-nodegroup

eksctl get cluster -A
eksctl get cluster -r us-east-1