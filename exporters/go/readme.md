#Build e run local:
go mod init exporter.go
go mod tidy
go build
./exporter

#Docker:
docker build -t gmaas2/go-exporter:0.1 .
docker run -d --name go-exporter -p 7788:7788 gmaas2/go-exporter:0.1
curl -GET localhost:7788/metrics