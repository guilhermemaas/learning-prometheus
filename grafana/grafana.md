#Pegar a senha do grafana:
kubectl get secret kube-prometheus-grafana -o jsonpath="{.data.admin-password}" -n monitoring| base64 --decode; echo

admin
prom-operator