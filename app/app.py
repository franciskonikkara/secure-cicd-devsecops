# Intentional Vulnerable App
from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure CI/CD Demo"

@app.route("/cmd")
def cmd():
    user_cmd = request.args.get("cmd")
    return os.popen(user_cmd).read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
