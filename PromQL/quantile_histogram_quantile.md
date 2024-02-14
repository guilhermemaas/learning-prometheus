quantile -> usar com summary
histogram_quantile -> usar com histogram

Servem pra pegar o percentil... 
0.95 -> Tempo de resposta de 95% das requests no período
0.75 -> Tempo de resposta de 75% das requests no período
0.70 -> Tempo de resposta de 70% das requests no período
quantile(0.99, prometheus_http_request_duration_seconds_bucket)

Dados de Histograma: Para que essa consulta funcione como esperado, a métrica prometheus_http_request_duration_seconds_bucket deve existir e ser do tipo histograma.
Uso do Percentil: O 99º percentil é um número comumente usado para medir a latência "pior caso" em aplicações web, ignorando as piores 1% das requisições que podem ser outliers.
Precisão dos Buckets: A precisão do 99º percentil calculado dependerá da granularidade dos buckets definidos para o histograma prometheus_http_request_duration_seconds_bucket.