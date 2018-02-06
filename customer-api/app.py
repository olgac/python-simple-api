from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def welcome():
    return "{ \"Welcome Customer\": \"%s\" }\n" % ( "2.0")

@app.route("/customer")
def customer():
    return "{ \"Time\": \"%s\", \"Host\": \"%s\", \"App\": \"%s\", \"Ver\": \"%s\" }\n" % (datetime.datetime.now().strftime("%H:%M:%S.%f"), socket.gethostname(), "Customer API", "2.0")

@app.route("/health")
def health():
    return "{ \"Status\": \"%s\" }\n" % ("UP")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)