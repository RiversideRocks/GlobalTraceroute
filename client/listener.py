from flask import Flask, Response, request
import json
from traceroute import run_traceroute, run_ping
import socket

def valid_ip(address):
    try: 
        socket.inet_aton(address)
        return True
    except:
        return False

app = Flask(__name__)

@app.route('/')
def home():
    return Response("Hello!", content_type="text/plain")

@app.route('/traceroute', methods=["POST"])
def trace():
    ip = ""
    try:
        ip = request.form["ip"]
        if valid_ip(ip):
            t = run_traceroute(ip)
            return Response(t, content_type="text/plain")
        else:
            return Response(json.dumps({"error": "invalid 'ip' param"}), content_type="application/json"), 400
    except:
        return Response(json.dumps({"error": "missing 'ip' param"}), content_type="application/json"), 400

@app.route('/ping', methods=["POST"])
def ping():
    ip = ""
    try:
        ip = request.form["ip"]
        if valid_ip(ip):
            t = run_ping(ip)
            return Response(t, content_type="text/plain")
        else:
            return Response(json.dumps({"error": "invalid 'ip' param"}), content_type="application/json"), 400
    except:
        return Response(json.dumps({"error": "missing 'ip' param"}), content_type="application/json"), 400

if __name__ == '__main__':
    app.run(debug=True)
