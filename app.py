from flask import Flask, jsonify
from flask import render_template
import json
from bson import json_util
import sqlite3
from vis import *

app = Flask(__name__)

src_IPlabels = get_Labels_src_IP()
src_IPvalues = get_occurances_src_IP()
Dest_IPlabels = get_Labels_DestIP()
Dest_IPvalues = get_occurances_DestIP()
Protocollabels = get_Labels_Protocol()
Protocolvalues = get_occurances_Protocol()
Src_Portlabels = get_Labels_Src_Port()
Src_Portvalues = get_occurances_Src_Port()
Dest_Portlabels = get_Labels_Dest_Port()
Dest_Portvalues = get_occurances_Dest_Port()

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/test")
def indexA():
    return render_template("try2.html")

@app.route("/pie")
def pie():
    return render_template("temp_plot.html")

@app.route("/src_IP")
def src_IP():
    return jsonify({'values': src_IPvalues, 'labels': src_IPlabels})

@app.route("/Dest_IP")
def Dest_IP():
    return jsonify({'values': Dest_IPvalues, 'labels': Dest_IPlabels})

@app.route("/Protocol")
def Protocol():
    return jsonify({'values': Protocolvalues, 'labels': Protocollabels})

@app.route("/Src_Port")
def Src_Port():
    return jsonify({'values': Src_Portvalues, 'labels': Src_Portlabels})

@app.route("/Dest_Port")
def Dest_Port():
    return jsonify({'values': Dest_Portvalues, 'labels': Dest_Portlabels})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)