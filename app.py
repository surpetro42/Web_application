from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def welcome_page():
    return render_template('main.html')
@app.route('/climatenet')
def climate():
    return render_template('climatenet.html')

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')
