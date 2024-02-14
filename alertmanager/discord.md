global:
  resolve_timeout: 30m
route:
  group_by: ['alertname']
  group_wait: 30s
  group_interval: 30s
  repeat_interval: 1h
  receiver: 'discord'
receivers:
- name: 'discord'
  discord_configs:
  - send_resolved: true
    webhook_url: 'https://discord.com/api/webhooks/1198351117873057964/AtRQsPbzGkX4HcSGvjGI7RF1X8mY4eYyGCrU1VYq7ej4jXnsLg9Mq_Ty4VL8XI8eV5vW'
    #icon_url: 'https://linuxtips.live/cdn/shop/files/LinuxTips_-_Full_HD_4cffe6bc-c489-48a4-a1e2-d8c5449b0242.png?v=1633560022&width=170'
    #title: |-
    #  [{{ .Status | toUpper }}{{ if eq .Status "firing" }}:{{ .Alerts.Firing | len }}
#{{ end }}] {{ .CommonLabels.alertname }} na instância {{ .CommonLabels.instance }}
inhibit_rules:
  - source_match:
      severity: 'critical'
    target_match:
      severity: 'warning'
    equal: ['alertname', 'dev', 'instance']