from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_conn():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_conn()
    posts = conn.execute("select * from posts").fetchall()
    return render_template("index.html", posts = posts)

@app.route("/posts/new", methods=("GET", "POST"))
def new():
    print("success")
    return render_template("new.html")
