FROM python:3.8-slim

LABEL maintenet "guilherme.maas@gmail.com"
LABEL description "Dockerfile for simple example of python prometheus exporter"

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

CMD python3 poe.py