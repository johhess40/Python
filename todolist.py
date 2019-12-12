#!usr/bin/python3
## Creating first todo list app, goal is to have entries write to the screen
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
## importing flask module and flask_sqlalchemy module


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///C:\Users\Student\Documents\GitHub\mycode\todo_service_flask\todo.db" ## path to the database file

db = SQLAlchemy(app)


class Todo(db.Model): ## database file format
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)


@app.route("/") ## define initial landing page
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    return render_template("index.html", incomplete=incomplete, complete=complete)
    ## query Todo table and return that query on landing page


@app.route("/add", methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()
    ## commiting submission to the database

    return redirect(url_for('index'))
    ## redirect result of the commit back to original landing page so that item is added to the list

@app.route("/complete/<id>")
def complete(id):
    todo = Todo.query.filter_by(id = int(id)).all()
    todo.complete = True
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(port=5004, debug=True)
