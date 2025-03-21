import requests, json
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome_page():
    return render_template("main.html")

@app.route('/climatenet', methods=['GET', 'POST'])
def climate():
    if request.method == 'POST':
        start_time = request.form.get('start_time')
        location = request.form.get('location')
        location = int(location)
    try:
        data = "No data available"
        info = None
        response = requests.get(f"https://emvnh9buoh.execute-api.us-east-1.amazonaws.com/getData?device_id={location}")
        data = response.json()
        if 'keys' in data:
            info = data['keys']
        else:
            data = "No key available"
        if 'data' in data:
            res = []
            for time in data['data']:
                if time[1] == start_time:
                    res.extend(time)
                else:
                    data = "No data available!!!!"
            data = res
            if not data:
                data = "No data available!!!!"
        else:
            data = "No data available"
    except:
        data = "There is no data yet"
    return render_template('climatenet.html', data=data, info=info)

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0', debug=True)
