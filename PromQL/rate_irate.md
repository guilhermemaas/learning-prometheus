#Rate
#Média de requests pro api/v1/query por segundo
rate(prometheus_http_requests_total{job="prometheus",handler="/api/v1/query"}[5m])

#Irate:
#Picos de requests pro api/v1/query por segundo
irate(prometheus_http_requests_total{job="prometheus",handler="/api/v1/query"}[5m])