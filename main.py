""""
Zachary Anthony
Python Linux Packet Sniffer
Linux systems only -
"""

import socket
import sys
from struct import *
import sqlite3
import init_db
import os
import plotly as py

init_db.setup()
init_db.creation()



tcp=6
udp=17
icmp=1

def ethernet_format(x):
    y = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(x[0]), ord(x[1]), ord(x[2]), ord(x[3]), ord(x[4]), ord(x[5]))
    return y

def collector():
    count = 0

    try:
        Link = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

    except socket.error, msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()


    try:
        while True:
            # Setup Stream information
            stream = Link.recvfrom(65565)
            stream = stream[0]
            ethernet_legnth = 14

            eheader = stream[:14]
            e = unpack('!6s6sh', eheader)
            # eproto = socket.ntohs(e[2])
            eproto = 8
            dest_Mac = ethernet_format(stream[0:6])
            src_Mac = ethernet_format(stream[6:12])

            if eproto == 8:
                count += 1

                # header information
                header_information = stream[ethernet_legnth:ethernet_legnth + 20]
                header_information = unpack('!BBHHHBBH4s4s', header_information)
                # Protocol Used
                proto = header_information[6]
                # Version Information
                vs = header_information[0]
                #TTL
                ttl= header_information[5]
                # Header length
                vs_x = vs >> 4
                x = vs & 0xF
                length = (x * 4)
                tot_length = length + ethernet_legnth

                # Src/Dest IP
                src_IP = socket.inet_ntoa(header_information[8])
                dest_IP = socket.inet_ntoa(header_information[9])

                # if proto == 6:
                # Port Information
                Zelda = stream[tot_length:tot_length + 20]
                tcp_header = unpack('!HHLLBBHHH', Zelda)

                src_PT = tcp_header[0]
                dest_PT = tcp_header[1]
                sequence = tcp_header[2]
                ack = tcp_header[3]
                test = tcp_header[4]
                test1 = tcp_header[5]

                print 'seq ' + str(sequence) + ' ack ' + str(ack)+ ' test ' + str(test)+ ' test1 ' + str(test1)


                init_db.use(count, src_Mac, dest_Mac, src_IP, src_PT, dest_IP, dest_PT, proto, ttl)

                #print str(count) + ' Protocol: ' + str(proto) + ' Source MAC: ' + str(
                #   src_Mac) + ' Destination MAC: ' + str(dest_Mac) + ' Source IP/Port: ' + str(src_IP) + '/' + str(
                #   src_PT) + ' Destination IP/Port: ' + str(dest_IP) + '/' + str(dest_PT)

    except KeyboardInterrupt:
        print "Working"


    os.system("sudo python vis.py")
    os.system("python run.py")




collector()



