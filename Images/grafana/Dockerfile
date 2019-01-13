FROM grafana/grafana

LABEL maintainer="AJDAINI Hatim <ajdaini.hatim@gmail.com>" \
      description="Grafana application with influxdb"

USER root

RUN apt-get update && \
    apt-get install -y \
    nano \
    && apt-get autoclean
