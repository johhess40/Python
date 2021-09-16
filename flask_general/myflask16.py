#!/usr/bin/python3

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/basic")
def basic():
    return render_template("hellobasic.html")

@app.route("/adv", defaults = {"name": "defaultuser"})
@app.route("/adv/<name>")
def adv(name):
    return render_template("helloadv.html", joevar = name)

@app.route("/scoretest/<int:score>")
def hell_name(score):
    return render_template("highscore.html", marks = score)


if __name__ == "__main__":
    app.run(port=5004)
