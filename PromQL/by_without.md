sum(prometheus_http_requests_total) by (code)
Ordenado e agrupado por code (http response code)


remove uma label da consulta/resultados
sum(prometheus_http_requests_total) without(job)