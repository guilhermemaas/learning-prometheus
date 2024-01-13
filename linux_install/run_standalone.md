#Download:
curl -LO https://github.com/prometheus/prometheus/releases/download/v2.48.1/prometheus-2.48.1.linux-amd64.tar.gz

#Decompactar:
tar -vxzf prometheus-2.48.1.linux-amd64.tar.gz

#Versão
./prometheus --version

#Acesso local
localhost:9090

#Exemplo de query:
process_cpu_seconds_total{job="prometheus"}[1m]
#Vai retornar 4 valores, por que o interval pro scrape tá 15s.
