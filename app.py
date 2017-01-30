from flask import Flask
from flask import render_template
import json
import pandas
import requests
import psycopg2
from sqlachemy import create_engine

app = Flask(__name__)

PSQL_HOST = 'acrn-db.cjqnnosw126f.us-east-1.rds.amazonaws.com'
USERNAME = 'andrew_norelli'
PASSWORD = 'flonkerton'
PSQL_PORT = 5432
DBS_NAME = 'workouts'
TABLE_NAMES = ['weight', 'runs_data', 'bike_data']

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/weight")
def weight():
	connection = create_engine('postgres://%s::%s@%s:%s/' + DBS_NAME) % (USERNAME, PASSWORD, PSQL_HOST, PSQL_PORT)
	connection.connect()

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)

