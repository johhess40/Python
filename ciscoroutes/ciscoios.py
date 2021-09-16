#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/ciscoios/")
def ciscoios():
    try:
        qparms = {}
        #user passes switchname= or default "bootstrapped switch"
        qparms["switchname"] = request.args.get("switchname", "bootstrapped switch")
        #user passes username= or default "admin"
        qparms["username"] = request.args.get("username", "admin")
        #user passes gateway= or default "0.0.0.0"
        qparms["defaultgateway"] = request.args.get("gateway", "0.0.0.0")
        #user passes ip= or default "0.0.0.0"
