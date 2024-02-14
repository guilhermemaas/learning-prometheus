#Para adicionar um novo target, basta adicionar no prometheus.yaml, abaixo de scrap_configs:
  - job_name: "dev-peoples-on-space-python"

    static_configs:
      - targets: ["192.168.1.119:8899"]

#Retornar na api todos os targets:
curl localhost:9090/api/v1/targets | jq .