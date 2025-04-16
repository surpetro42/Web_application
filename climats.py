import requests
from flask import request, render_template

def climate_route():
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
                for time in data['data'][::-1]:
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
    return render_template('climatenet.html', data=None, info=None)
