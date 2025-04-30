import sqlite3
import requests, json
import climats, work, me, useradd
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

def init_db():
    bridge = sqlite3.connect("user.db")
    c = bridge.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL (length(password) >= 8))''')
    bridge.cimmit()
    bridge.close()

@app.route('/')
def welcome_page():
    return render_template("main.html")
    # return useradd.useradd_rute()

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            bridge = sqlite3.connect("users.db")
            c = bridge.cursor()
            c.execut("INSERT INFO user (username, password) VALUE (?, ?)", (username, password))
            bridge.cimmit()
            bridge.close()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            error = "The user exists!"
    return render_template("register.html", error=error)


@app.route('/login')
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        bridge = sqlite3.connect("users.db")
        c = bridge.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        bridge.cimmit()
        bridge.close()
        if user:
            return f"Welcome, {username}!"
        else:
            error = "Invalid username or password"
    return render_template("login.html", error=error)


@app.route('/work')
def three_months_work():
    return work.work_route()
    
    
@app.route('/climatenet', methods=['GET', 'POST'])
def climate():
    return climats.climate_route()

@app.route('/me')
def aboutme():
    return me.me_route()

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0', debug=True)
