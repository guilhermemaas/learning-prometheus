- Focado em máquinas linux.

Download:
wget https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz
tar -xvzf node_exporter-1.7.0.linux-amd64.tar.gz
sudo mv node_exporter /usr/local/bin
node_exporter --version

Adicionar usuário e grupo de usuários:
sudo addgroup --system node_exporter
sudo adduser --shell /bin/nologin --system --group node_exporter

Criação do serviço:
vim /etc/systemd/system/node_exporter.service

[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target

systemctl daemon-reload
systemctl active node_exporter
systemctl restart node_exporter

curl -GET http://localhost:9090/api/v1/query --data-urlencode "query=node_cpu_seconds_total{job='node-exporter-prometheus-linux'}" | jq .