import json

from flask import Flask

import weather


app = Flask(__name__)


@app.route("/")
def hello():
	return "Hello, World!"


@app.route("/weather/")
def weather_route():
	temp = weather.weather()
	temp = json.dumps(temp)
	return temp


@app.route("/weather/my-cities/")
def weather_multiple_citites():
	return "Cluj: 15, New York: 10"
