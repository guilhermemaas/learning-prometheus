Clonar o repositório:
git clone https://github.com/prometheus-operator/kube-prometheus.git

#Instalar os CRDS (Extender o k8s, adicionando novas apis)
kubectl create -f manifests/setup/

#Novas apis
kubectl api-resources

#Um dos CRDs:
k get servicemonitor -A

#instalar os objetos da stack
kubectl apply -f manifests

#Acessando o Grafana:
kubectl port-forward -n monitoring svc/grafana 33000:3000

#Pegar os service monitors:
kubectl get servicemonitors grafana -n monitoring -o yaml

#Pegar a senha do admin do grafana:
kubectl get secret kube-prometheus-grafana -o jsonpath="{.data.admin-password}" -n monitoring| base64 --decode; echo

#Acessando o promethues:
kubectl port-forward -n monitoring svc/kube-prometheus-kube-prome-prometheus 39090:9090