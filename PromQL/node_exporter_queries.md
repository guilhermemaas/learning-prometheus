###CPU

Percentual de idle de cpu:
100 - avg by (cpu) (irate(node_cpu_seconds_total{job='node-exporter-prometheus-linux', mode="idle"}[5m])) * 100
100 - média ordenado por cpu, irate = dois últimos pontos de métrica * 100.

Sem percentual:
avg by (cpu) (irate(node_cpu_seconds_total{job='node-exporter-prometheus-linux', mode="idle"}[5m]))


###Memória
Percentual de memória em uso:
100 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100

Total livre:
node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes

###Disco:
Percentual de utilização do /
100 - (node_filesystem_avail_bytes{job="node-exporter-prometheus-linux",mountpoint="/"} / node_filesystem_size_bytes{job="node-exporter-prometheus-linux",mountpoint="/"}) * 100


Total de disco livre em GB:
(node_filesystem_size_bytes{job="node-exporter-prometheus-linux",mountpoint="/"} - node_filesystem_avail_bytes{job="node-exporter-prometheus-linux",mountpoint="/"}) / 1024 / 1024 / 1024