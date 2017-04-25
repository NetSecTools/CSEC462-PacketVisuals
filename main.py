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

try:
    Link = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

except socket.error, msg:
    print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()


while True:
    # Setup Stream information
    stream = Link.recvfrom(65565)
    stream = stream[0]

    #header information
    header_information = stream[0:20]
    header_information = unpack('!BBHHHBBH4s4s', header_information)
    #Protocol Used
    proto = str(header_information[6])

    #Src/Dest IP
    src_IP = str(socket.inet_ntoa(header_information[8]))
    dest_IP = str(socket.inet_ntoa(header_information[9]))


    # Version Information
    vs = header_information[0]
    # Header length
    vs_x = vs >> 4
    x = vs & 0xF

    #Port Information
    length = (x * 4)
    length20 = length + 20
    Zelda = stream[length:length20]
    port_info = unpack('!HHLLBBHHH', Zelda)

    src_PT = str(port_info[0])
    dest_PT = str(port_info[1])

    init_db.setup()
    init_db.creation()
    init_db.use(proto, src_IP, src_PT, dest_IP, dest_PT)

    #print 'Version : ' + str(vs_x) + ' IP Header Length : ' + str(x) + ' Protocol ' + str(protocol_used) + ' Source IP ' + str(src_IP) + ' Destination IP ' + str(dest_IP)
    print 'Protocol: ' + proto + ' Source IP/Port: ' + src_IP + '/' + src_PT + ' Destination IP/Port: ' + dest_IP + '/' + dest_PT



