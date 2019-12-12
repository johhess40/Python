#!usr/bin/python3
## Creating first todo list app, goal is to have entries write to the screen
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

## importing flask module and flask_sqlalchemy module


app = Flask(__name__)

# define where DB lives
app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///C:\Users\Galileo\Documents\GitHub\mycode\todo_service_flask\todo.db" ## path to the database file

db = SQLAlchemy(app)


#### ENSURE OUR DATABASE AND TABLE INSIDE THE DATABASE HAVE BEEN CREATED ####
## connect to the DB
conn = sqlite3.connect('todo.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor()                  # The database will be saved in the location where your 'py' file is saved
# Create table - Todo
c.execute('''CREATE TABLE IF NOT EXISTS Todo
             ([id] INTEGER PRIMARY KEY AUTOINCREMENT,[text] text, [complete] integer)''')
## write out the changes
conn.commit()
#close the connection
conn.close()


class Todo(db.Model): ## database file format
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)


@app.route("/") ## define initial landing page
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    # print(incomplete)
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

@app.route("/complete/<int:id>")
def complete(id):
    singletodo = Todo.query.filter_by(id=id).first()
    singletodo.complete = True
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(port=5004, debug=True)
