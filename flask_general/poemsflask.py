#/usr/bin/python3

import json
import random
import requests

from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

# @app.route("/poems")
#def jays_poems():
    #return render_template("jays_poems.html")
@app.route("/")
@app.route("/index")
def home():
    return '<a href ="/jays_poems/">jays_poems<a>'

@app.route("/jays_poems/<pn>")
def send(pn):
    with open("poems.json") as jp:
        jp = json.load(jp)
    if jp.get(pn):
        return jp.get(pn)

    else:
        return "the key does not exist"

@app.route("/chuck")
def chucksjokes():
    r = requests.get("https://api.chucknorris.io/jokes/random")
    guy = r.json()
    print(guy["value"])


if __name__ == "__main__":
    app.run(port=5004)
