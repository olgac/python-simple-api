FROM python:3.8.1-alpine3.11
WORKDIR /usr/local/bin
RUN pip install flask requests
COPY app.py .
CMD [ "python", "./app.py" ]