Mais usado com counter, mas dá pra usar com gauge, summary e histogram.

sum(go_memstats_alloc_bytes{job="prometheus"})
sum(go_memstats_alloc_bytes)

contar todas as métricas, na verdade é o total de métricas nesse caso:
count(prometheus_http_requests_total)

se quisesse somar o total de requests de todas as chamadas, de todos os handlers(paths) seria:
sum(prometheus_http_requests_total)

