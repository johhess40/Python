#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    x = 1

    y = 2

    return f"The results of {x} plus {y} is equal to {x+y}"

@app.route("/bond")
def bond():
    return f"Bond, James Bond 007, welcome back to MI6"

@app.route("/secretagent/<donumber>")
def britishagent(donumber):
    return f"Hello secret agent {donumber}. We have an assignment for you."


if __name__ == "__main__":
    app.run(port=5004)
