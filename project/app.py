from flask import Flask
from flask import render_template
import json
from bson import json_util
import sqlite3
from vis import get_Labels, get_occurances, get_max_size

app = Flask(__name__)

Labels = get_Labels()
Occurrances = get_occurances()
maxsize=get_max_size()
print maxsize

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/try")
def chart():

    labels = Labels
    values = Occurrances
    return render_template('chart.html', values=values, labels=labels, maxsize=maxsize)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)