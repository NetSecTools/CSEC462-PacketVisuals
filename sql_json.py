import json
import collections
# !/bin/python

import sqlite3



def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect("store.db")
connection.row_factory = dict_factory

cursor = connection.cursor()

cursor.execute("select Number, Src_MAC, Dest_MAC, Src_IP, Src_Port, Dest_IP, Dest_Port, Protocol from store")

# fetch all or one we'll go for all.

results = cursor.fetchall()
st = "store.js"
f = open(st, 'w')
print >> f, results

connection.close()
