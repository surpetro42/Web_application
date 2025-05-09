import requests, json
import climats, work, me, user, accaunt
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome_page():
    return render_template("main.html")

@app.route("/SignIn", methods=["GET", "POST"])
def register():
    user.init_db()
    return user.register()

@app.route("/LogIn", methods=["GET", "POST"])
def login():
    user.init_db()
    return user.login()

@app.route("/user/<username>")
def profile(username):
    return accaunt.user_profile(username)

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
