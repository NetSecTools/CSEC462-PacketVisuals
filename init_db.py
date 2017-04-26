'''
Zachary Anthony
Initializes a SQL database that will store information sent from main.py

'''

import sqlite3

conn = sqlite3.connect('store.db')
c = conn.cursor()

def setup():
    conn = sqlite3.connect('store.db')
    c = conn.cursor()

def creation():
    c.execute('DROP TABLE IF EXISTS Store')
    c.execute('CREATE TABLE Store (Src_MAC varchar(15), Dest_MAC varchar(15), Src_IP varchar(15), Src_Port varchar(15), Dest_IP varchar(15), Dest_Port varchar(15), Protocol int)')
    conn.commit()

def use(str1, str2, str3, str4, str5, str6, str7):

    #Prevents SQL injection attacks, rather than using hardcoded strings
    c.execute("INSERT INTO Store VALUES (?, ?, ?, ?, ?, ?, ?)", (str1, str2, str3, str4, str5, str6, str7))
    conn.commit()

