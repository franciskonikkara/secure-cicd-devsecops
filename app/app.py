# Intentional Vulnerable App

from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/cmd")
def cmd():
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()
