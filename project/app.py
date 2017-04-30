from flask import Flask
from flask import render_template
import json
from bson import json_util
import sqlite3
from vis import get_Labels, get_occurances

app = Flask(__name__)

Labels = get_Labels()
Occurrances = get_occurances()


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/test")
def indexA():
    return render_template("indexA.html")
@app.route("/real")
def indexAA():
    return render_template("indexAA.html")

@app.route("/try")
def chart():

    labels = Labels
    values = Occurrances
    return render_template('chart.html', values=values, labels=labels)

@app.route("/home")
def donorschoose_projects():
    #connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    #collection = connection[DBS_NAME][COLLECTION_NAME]
    #projects = collection.find(projection=FIELDS)

    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT Src_IP, Dest_IP FROM store""")
    rows = cursor.fetchall()
    json_projects = []
    for row in rows:
        json_projects.append(row)
    json_projects = json.dumps(json_projects, default=json_util.default)
    conn.close()
    return json_projects

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)