#!/usr/bin/python3
## creating a helper function for to do list app in flask
## defining statuses and connecting to sql database

import sqlite3


DB_PATH = "./todo.db"
NOTSTARTED = "Not Started"
INPROGRESS = "In Progress"
COMPLETE = "Completed"

def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor() ## use the cursor after making the connection

        c.execute("insert into items(item, status) values(?,?)", (item(NOTSTARTED))


        conn.commit() ## commit to save changes to database

    return{"item": item, "status": NOTSTARTED}
except Exception as e:
    print("Error: ", e)
    return None
