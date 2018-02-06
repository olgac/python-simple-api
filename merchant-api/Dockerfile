FROM python:alpine

MAINTAINER Ahmet Vehbi Olgaç, ahmetvehbiolgac@gmail.com

ENV Environmet=DEV

LABEL Group="API"

EXPOSE 8080

WORKDIR /var/local/

VOLUME ["/var/log", "/var/empty"]

COPY app.py .

RUN echo $(date) Customer API runs on $HOSTNAME >> /var/log/api.log && pip install flask

HEALTHCHECK --interval=5s --timeout=3s --retries=3 CMD curl -f http://localhost:8080/health || exit 1

CMD [ "python", "./app.py" ]