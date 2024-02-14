###Criar um config com o collector, e ajustar as permissões:

sudo vim /etc/node_exporter/node_export.conf
OPTIONS="--collector.systemd"
https://github.com/prometheus/node_exporter?tab=readme-ov-file#disabled-by-default
sudo chown -R node_exporter:node_exporter /etc/node_exporter/

###Alterar o arquivo do systemd
sudo vim /etc/systemd/system/node_exporter.service

[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
EnvironmentFile=/etc/node_exporter/node_exporter.options
ExecStart=/usr/local/bin/node_exporter $OPTIONS

[Install]
WantedBy=multi-user.target

###Reiniciar o node_exporter
sudo systemctl daemon-reload
sudo systemctl restart node_exporter

