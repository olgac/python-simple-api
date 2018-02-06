FROM python:alpine

WORKDIR /var/local/

COPY app.py .

RUN pip install flask

HEALTHCHECK --interval=5s --timeout=3s --retries=3 CMD curl -f http://localhost:8080/health || exit 1

CMD [ "python", "./app.py" ]