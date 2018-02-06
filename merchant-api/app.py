from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/merchant-info")
def info():
    return "{ \"Datetime\": \"%s\", \"Hostname\": \"%s\", \"Application\": \"%s\", \"Verison\": \"%s\" }\n" % (datetime.datetime.now().strftime("%H:%M:%S.%f"), socket.gethostname(), "Merchant", "2.0")

@app.route("/health")
def health():
    return "{ \"Status\": \"%s\" }\n" % ("UP")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)