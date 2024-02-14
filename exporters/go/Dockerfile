FROM golang:1.19.0-alpine3.16 AS build

WORKDIR /app
COPY . .

RUN go build exporter.go

FROM alpine:3.16

WORKDIR /app
COPY --from=build /app/exporter .

EXPOSE 7788

CMD ["./exporter"]