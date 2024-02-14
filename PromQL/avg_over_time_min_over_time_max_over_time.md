É o o min,max e avg ao longo do tempo.

avg_over_time(prometheus_http_requests_total[7d])

max_over_time(prometheus_http_requests_total{handler="/api/v1/query",code="200"}[7d])

sum_over_time(prometheus_http_requests_total{handler="/api/v1/query",code="200"}[7d])

stddev_over_time(prometheus_http_requests_total{handler="/api/v1/query",code="200"}[7d])
Maior variação no período. Os 2 pontos mais distantes da média dos valores no período.
Detecção de anomalia.

