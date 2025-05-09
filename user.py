from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import main

def init_db():
    bridge = sqlite3.connect("users.db")
    c = bridge.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    bridge.commit()
    bridge.close()

def register():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            bridge = sqlite3.connect("users.db")
            c = bridge.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            bridge.commit()
            bridge.close()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            error = "The user exists!"
    return render_template("register.html", error=error)

def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        bridge = sqlite3.connect("users.db")
        bridge.row_factory = sqlite3.Row
        c = bridge.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        bridge.close()

        if user:
            return main.profile(user)
        else:
            error = "Invalid username or password"
    return render_template("login.html", error=error)