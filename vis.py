"""
Zachary Anthony
Pandas framework visualization
"""

import sqlite3
import csv
from csv import DictReader

'''
Source IP vs Count --> csv
'''

def src_IPcount():

    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("""Select src_IP, COUNT(src_IP) from store GROUP BY Src_IP""")

    with open("src_IP.csv", "wb") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        cursor.execute("""Select src_IP, COUNT(src_IP) from store GROUP BY Src_IP""")
        rows = cursor.fetchall()
        csv_writer.writerows(rows)

def get_Labels_src_IP():
    with open("src_IP.csv") as f:
        a1 = [row["Src_IP"] for row in DictReader(f)]
        f.close()
        return a1

def get_occurances_src_IP():
    with open("src_IP.csv") as x:
        a2 = [row["COUNT(src_IP)"]for row in DictReader(x)]
        x.close()
        return a2

'''
Destination IP vs Count --> csv
'''

def dest_IPcount():

    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("""Select dest_IP, COUNT(dest_IP) from store GROUP BY dest_IP""")

    with open("dest_IP.csv", "wb") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        cursor.execute("""Select dest_IP, COUNT(dest_IP) from store GROUP BY dest_IP""")
        rows = cursor.fetchall()
        csv_writer.writerows(rows)

def get_Labels_DestIP():
    with open("dest_IP.csv") as f:
        a1 = [row["Dest_IP"] for row in DictReader(f)]
        f.close()
        return a1


def get_occurances_DestIP():
    with open("dest_IP.csv") as x:
        a2 = [row["COUNT(dest_IP)"]for row in DictReader(x)]
        x.close()
        return a2

''''
Protocol vs Count(Protocol) --> csv
'''

def Protocolcount():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("""Select Protocol, COUNT(Protocol) from store GROUP BY Protocol""")
    with open("Protocol.csv", "wb") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        cursor.execute("""Select Protocol, COUNT(Protocol) from store GROUP BY Protocol""")
        rows = cursor.fetchall()
        csv_writer.writerows(rows)

def get_Labels_Protocol():
    with open("Protocol.csv") as f:
        a1 = [row["Protocol"] for row in DictReader(f)]
        f.close()
        return a1
def get_occurances_Protocol():
    with open("Protocol.csv") as x:
        a2 = [row["COUNT(Protocol)"]for row in DictReader(x)]
        x.close()
        return a2

'''
Source_Port vs COUNT(Source Port) --> csv
'''

def Src_Portcount():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("""Select Src_Port, COUNT(Src_Port) from store GROUP BY Src_Port ORDER BY COUNT(Src_Port) DESC LIMIT 10""")
    with open("Src_Port.csv", "wb") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        cursor.execute("""Select Src_Port, COUNT(Src_Port) from store GROUP BY Src_Port ORDER BY COUNT(Src_Port) DESC LIMIT 10""")
        rows = cursor.fetchall()
        csv_writer.writerows(rows)
def get_Labels_Src_Port():
    with open("Src_Port.csv") as f:
        a1 = [row["Src_Port"] for row in DictReader(f)]
        f.close()
        return a1
def get_occurances_Src_Port():
    with open("Src_Port.csv") as x:
        a2 = [row["COUNT(Src_Port)"]for row in DictReader(x)]
        x.close()
        return a2

'''
Destination Port vs COUNT(Destination Port) --> csv
'''

def Dest_Portcount():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("""Select Dest_Port, COUNT(Dest_Port) from store GROUP BY Dest_Port ORDER BY COUNT(Dest_Port) DESC LIMIT 10""")
    with open("Dest_Port.csv", "wb") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        cursor.execute("""Select Dest_Port, COUNT(Dest_Port) from store GROUP BY Dest_Port ORDER BY COUNT(Dest_Port) DESC LIMIT 10""")
        rows = cursor.fetchall()
        csv_writer.writerows(rows)

def get_Labels_Dest_Port():
    with open("Dest_Port.csv") as f:
        a1 = [row["Dest_Port"] for row in DictReader(f)]
        f.close()
        return a1

def get_occurances_Dest_Port():
    with open("Dest_Port.csv") as x:
        a2 = [row["COUNT(Dest_Port)"]for row in DictReader(x)]
        x.close()
        return a2

src_IPcount()
dest_IPcount()
Protocolcount()
Src_Portcount()
Dest_Portcount()