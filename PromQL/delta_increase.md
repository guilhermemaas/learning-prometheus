###Delta
Serve pra pegar a diferença entre 2 momentos distintos:
Por exemplo, quanto que cresceu o disco de um dia pro outro. Diferença em GBs, por exemplo.

delta(prometheus_http_response_size_bytes_count{handler="/api/v1/query"}[5m])

Muito bom pra IO de disco, uso de rede... Pra analisar a variação.


###Increase

increase(prometheus_http_requests_total{handler="/api/v1/query",code="200"}[5m])

Bom para entender o quanto que aumentou no período, é bom pra count também.

