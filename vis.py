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


def pretty_picture():

    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("""Select src_IP, COUNT(src_IP) from store GROUP BY Src_IP""")
    rows = cursor.fetchall()
    print rows

    data_list = []
    '''
    for spot in rows:
        data_dict = {
            'name': spot[0],
            'imports': spot[1]}
        data_list.append(data_dict)
    data_agg = json.dumps(data_list)
    f = open('data.json', 'w')
    print >> f , rows
    f.close()
    '''
    with open("out.csv", "wb") as csv_file:  # Python 2 version
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])  # write headers
        cursor.execute("""Select src_IP, COUNT(src_IP) from store GROUP BY Src_IP""")
        rows = cursor.fetchall()
        csv_writer.writerows(rows)

def get_Labels():
    with open("out.csv") as f:
        a1 = [row["Src_IP"] for row in DictReader(f)]
        f.close()
        return a1


def get_occurances():
    with open("out.csv") as x:
        a2 = [row["COUNT(src_IP)"]for row in DictReader(x)]
        x.close()
        return a2

    """
    json_projects = []
    for row in rows:
        json_projects.append(row)
    json_projects = json.dumps(json_projects, default=json_util.default)
    conn.close()
    print json_projects
    f = open('data.json', 'w')
    print >> f, json_projects
    f.close()
    """
pretty_picture()

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