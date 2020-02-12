from flask import Flask, jsonify
import os
import time
import requests

app = Flask(__name__)

API = os.getenv('API')
HOST = os.uname()[1]
NAME = os.getenv('NAME')
ENV = os.getenv('ENV')
VERSION = os.getenv('VERSION')

@app.route("/")
def root():
    return jsonify(time=time.time(), host=HOST, name=NAME, env=ENV, version=VERSION)

@app.route("/live")
def live():
    return jsonify(status='OK')

@app.route("/ready")
def ready():
    return jsonify(status='OK')

@app.route("/connect")
def connect():
    return jsonify(requests.get(API).json())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)