#Exemplo:
windows_exporter-0.25.0-amd64.exe --collectors.enabled "cpu,process" --collector.process.include="(chrome)"

#Com config:
---
# Note this is not an exhaustive list of all configuration values
collectors:
  enabled: cpu,cs,logical_disk,net,os,service,system,textfile
collector:
  service:
    services-where: Name='windows_exporter'
  scheduled_task:
    include: /Microsoft/.+
log:
  level: debug
scrape:
  timeout-margin: 0.5
telemetry:
  path: /metrics
  max-requests: 5
web:
  listen-address: ":9182"

windows_exporter-0.25.0-amd64.exe --config.file=config.yaml

