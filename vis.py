"""
Zachary Anthony
Pandas framework visualization
"""

import sqlite3
import json
from bson import json_util
import flask
import csv
from csv import DictReader
import os


def pretty_picture():

    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("""Select src_IP, COUNT(src_IP) from store GROUP BY Src_IP""")
    rows = cursor.fetchall()
    #print rows
    #os.system("rm out.csv")

    with open("out.csv", "wb") as csv_file:  # Python 2 version
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])  # write headers
        cursor.execute("""Select src_IP, COUNT(src_IP) from store GROUP BY Src_IP""")
        rows = cursor.fetchall()
        csv_writer.writerows(rows)
    #os.system("cp out.csv /project/")

def get_Labels():
    with open(os.path.join("out.csv")) as f:
        a1 = [row["Src_IP"] for row in DictReader(f)]
        f.close()
        return a1


def get_occurances():
    with open("out.csv") as x:
        a2 = [row["COUNT(src_IP)"]for row in DictReader(x)]
        x.close()
        return a2

def get_max_size():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("Select COUNT(src_IP) AS ct from store GROUP BY src_IP ORDER BY COUNT(src_IP) DESC LIMIT 1")
    size = cursor.fetchone()[0]
    return size

def test():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("""Select src_IP from store""")
    rows = cursor.fetchall()
    string = []
    for row in rows:
        string.append(row)

    print string

#test()

pretty_picture()