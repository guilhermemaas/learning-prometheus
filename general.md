Visão Geral:

Dentre os pilares da observabilidade, o Prometheus é responsável por coletar e armazenar métricas (Métricas, Traces e Logs).
O Prometheus também um TSDB, Time Series Database.

Agent tradicional x Exporter:
O Prometheus se baseia em exporters, ou seja, pro prometheus coletar algo, ele precisa ter um exporter/endpoint disponível para buscar as métricas.
Pode rodar em um server Linux, em um Node, ou então um endpoint numa aplicação(/metrics), métricas chave valor.

Porém, em algumas ocasiões (Firewall) pode receber ao invés de coletar, com push gateway (Um firewall por exemplo).

Métricas: Prometheus, Datadog, NewRelic
Traces: Tempo, ELK, Datadog
Logs: Loky, Greylog, ELK, Datadog
Eventos: Zabbix?

Arquitetura:
- Storage: TSDB.
- Retrieval: 
    - Coleta as métricas e armazena no TSDB. 
    - Ele conversa com os Jobs/exporters (E também com o Push/Gateway pra receber dados). 
    - Vai buscar as métricas nos exportes e gravar no storage.
    - Service Discovery (Services do k8s/Consul se registram, ou DNS).
- PromQL: Queries/Pesquisas é a linguagem de buscas nas métricas, ou coorelacionar.
- Outros Prometheus (Federation).

/metrics:
net_conntrack_dialer_conn_failed_total{dialer_name="alertmanager",reason="resolution"} 0
Nome da métrica | {Labels} | Valor

prometheus.yml:
global: # Configurações globais do Prometheus, ou seja, configurações que serão utilizadas em todos os jobs caso não sejam configuradas separadamente dentro de cada job.
  
  scrape_interval: 15s # Intervalo de coleta dos dados, ou seja, a cada 15 segundos o Prometheus vai até o alvo monitorado coletar as métricas, o padrão é 1 minuto.
  
  evaluation_interval: 15s # Intervalo para o Prometheus avaliar as regras de alerta, o padrão é 1 minuto. Não estamos utilizando regras para os alertas, vamos manter aqui somente para referência.

  scrape_timeout: 10s # Intervalos para o Prometheus aguardar o alvo monitorado responder antes de considerar que o alvo está indisponível, o padrão é 10 segundos.

rule_files: # Inicio da definição das regras de alerta, nesse primeiro exemplo vamos deixar sem regras, pois não iremos utilizar alertas por agora.

scrape_configs: # Inicio da definição das configurações de coleta, ou seja, como o Prometheus vai coletar as métricas e onde ele vai encontrar essas métricas.

  - job_name: "prometheus" # Nome do job, ou seja, o nome do serviço que o Prometheus vai monitorar.

    static_configs: # Inicio da definição das configurações estáticas, ou seja, configurações que não serão alteradas durante o processo de coleta.

      - targets: ["localhost:9090"] # Endereço do alvo monitorado, ou seja, o endereço do serviço que o Prometheus vai monitorar. Nesse caso é o próprio Prometheus.