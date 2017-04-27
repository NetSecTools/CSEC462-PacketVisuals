'''
Zachary Anthony
Initializes a SQL database that will store information sent from main.py

'''

import sqlite3
import json

conn = sqlite3.connect('store.db')
c = conn.cursor()

def setup():
    conn = sqlite3.connect('store.db')
    c = conn.cursor()

def creation():
    c.execute('DROP TABLE IF EXISTS Store')
    c.execute('CREATE TABLE Store (Number varchar(255), Src_MAC varchar(15), Dest_MAC varchar(15), Src_IP varchar(15), Src_Port varchar(15), Dest_IP varchar(15), Dest_Port varchar(15), Protocol int)')
    conn.commit()

def use(str1, str2, str3, str4, str5, str6, str7, str8):

    #Prevents SQL injection attacks, rather than using hardcoded strings
    c.execute("INSERT INTO Store VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (str1, str2, str3, str4, str5, str6, str7, str8))
    conn.commit()

def JSON():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT Number, Src_MAC, Dest_MAC, Src_IP, Src_Port, Dest_IP, Dest_Port, Protocol FROM Store""")

    rows = cursor.fetchall()

    rowarray_list = []
    for row in rows:
        t = (row.Number, row.Src_MAC, row.Dest_MAC, row.Src_IP,
             row.Src_Port, row.Dest_IP, row.Dest_Port, row.Protocol)
        rowarray_list.append(t)

    j = json.dumps(rowarray_list)
    rowarrays_file = 'store_rowarrays.js'
    f = open(rowarrays_file, 'w')
    print >> f, j

    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['Number'] = row.Number
        d['Src_MAC'] = row.Src_MAC
        d['Dest_MAC'] = row.Dest_MAC
        d['Src_IP'] = row.Src_IP
        d['Src_Port'] = row.Src_Port
        d['Dest_IP'] = row.Dest_IP
        d['Dest_Port'] = row.Dest_port
        d['Protocol'] = row.Protocol
        objects_list.append(d)

    j = json.dumps(objects_list)
    objects_file = 'store_objects.js'
    f = open(objects_file, 'w')
    print >> f, j

    conn.close()

