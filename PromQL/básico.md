#PROMQL -> Prometheus Query Language

net_conntrack_dialer_conn_failed_total{dialer_name="alertmanager",reason="resolution"} 0
Nome da métrica | {Labels} | Valor

##Targets disponíveis:
up

##Fazer uma consulta PromQL via api
curl -GET localhost:9090/api/v1/query --data-urlencode "query=up" | jq .

#Data Model - Prometheus:

metrica{nome_label="valor_label"}3

##Exemplos:

###up
up{instance="localhost:9090", job="prometheus"}
up{instance="localhost:9090", job="prometheus"}

últimos 10 min:
up{instance="localhost:9090"}[10m]

último dia:
up{instance="localhost:9090"}[1d]

último mês:
up{instance="localhost:9090"}[1w]


