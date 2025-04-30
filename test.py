from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Шаблоны
register_template = '''
<h2>Регистрация</h2>
<form method="POST">
  <input type="text" name="username" placeholder="Логин"><br>
  <input type="password" name="password" placeholder="Пароль"><br>
  <input type="submit" value="Зарегистрироваться">
</form>
{% if error %}
<p style="color:red;">{{ error }}</p>
{% endif %}
<a href="/login">Уже есть аккаунт?</a>
'''

login_template = '''
<h2>Вход</h2>
<form method="POST">
  <input type="text" name="username" placeholder="Логин"><br>
  <input type="password" name="password" placeholder="Пароль"><br>
  <input type="submit" value="Войти">
</form>
{% if error %}
<p style="color:red;">{{ error }}</p>
{% endif %}
<a href="/register">Регистрация</a>
'''

# Создание базы и таблицы
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            conn = sqlite3.connect("users.db")
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            error = "Пользователь уже существует"
    return render_template_string(register_template, error=error)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            return f"Добро пожаловать, {username}!"
        else:
            error = "Неверный логин или пароль"
    return render_template_string(login_template, error=error)

@app.route("/")
def index():
    return redirect(url_for("login"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
