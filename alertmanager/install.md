wget https://github.com/prometheus/alertmanager/releases/download/v0.26.0/alertmanager-0.26.0.linux-386.tar.gz

wget https://github.com/prometheus/alertmanager/releases/download/v0.26.0/alertmanager-0.26.0.linux-386.tar.gz
tar -xvzf alertmanager-0.26.0.linux-386.tar.gz
cd alertmanager-0.26.0.darwin-amd64/
sudo cp alertmanager /usr/local/bin/
sudo cp amtool /usr/local/bin/
mkdir -p /etc/alertmanager
mkdir -p /etc/alertmanager
cp alertmanager.yml /etc/alertmanager/

Criar um grupo pro Alert Manager:
sudo groupadd -f alertmanager

Criar um usuário pro Alet Manager:
sudo useradd -r -g alertmanager --no-create-home --shell /bin/false alertmanager

id alertmanager:
id alertmanager
uid=997(alertmanager) gid=1001(alertmanager) groups=1001(alertmanager)

Obs.: ID de usuário menor que 1.000 são usuários de sistema, superior, convencionais.

Diretório de templates:
sudo mkdir /etc/alertmanager/templates

sudo chown -R alertmanager:alertmanager /usr/local/bin/alertmanager
sudo chown -R alertmanager:alertmanager /etc/alertmanager

sudo mkdir /var/lib/alertmanager
sudo chown -R alertmanager:alertmanager /var/lib/alertmanager/

Instalar o service:
cat /etc/systemd/system/alertmanager.service
[Unit]
Description=Prometheus Alert Manager Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/alertmanager \
  --config.file=/etc/alertmanager/alertmanager.yml \
  --web.route-prefix=/

[Install]
WantedBy=multi-user.target

#Config default (/etc/alertmanager/alertmanager.yml):
route:
  group_by: ['alertname'] #Agrue os alertas por nome do alerta
  group_wait: 30s #30 segundos antes de alertar
  group_interval: 5m #Quando vai atualizar o grupo de alertas após começar a ocorrer, quando vai adicionar um novo alerta no grupo. Talvez diminuir pra 1min, por exemplo. Se entra uma nova máquina nesse alerta, por exemplo, quanto tempo demora pra aparecer.
  repeat_interval: 1h # Não mudou o status do alerta, após quanto tempo vai mandar o alerta novamente (No slack, teams, etc)
  receiver: 'web.hook' #O Receiver que vai receber o alerta
receivers: discord#Configuraçã do receiver (Slack, Discord, Teams, etc)
  - name: 'web.hook'
    webhook_configs:
      - url: 'http://127.0.0.1:5001/'
inhibit_rules: #Inibição de alertas
  - source_match:
      severity: 'critical'
    target_match:
      severity: 'warning'
    equal: ['alertname', 'dev', 'instance'] #Por exemplo, se tivermos um critical que o cluster caiu, não alertar 
    os warnings e tudo mais de todas as apps que pararam de rodar também.