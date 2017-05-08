import plotly as py
import plotly.graph_objs as go
import vis

src_IPlabels = vis.get_Labels_src_IP()
src_IPvalues = vis.get_occurances_src_IP()
Dest_IPlabels = vis.get_Labels_DestIP()
Dest_IPvalues = vis.get_occurances_DestIP()
Protocollabels = vis.get_Labels_Protocol()
Protocolvalues = vis.get_occurances_Protocol()
Src_Portlabels = vis.get_Labels_Src_Port()
Src_Portvalues = vis.get_occurances_Src_Port()
Dest_Portlabels = vis.get_Labels_Dest_Port()
Dest_Portvalues = vis.get_occurances_Dest_Port()
ttl_values = vis.get_occurances_ttl()
ttl_labels = vis.get_Labels_ttl()


def src_IP():
    figA = {
        'data': [{'labels': src_IPlabels,
                  'values': src_IPvalues,
                  'type': 'pie'}],
        'layout': {'title': 'Source IP vs # of packets'}
         }

    py.offline.plot(figA)

def dest_IP():
    figB = {
        'data': [{'labels': Dest_IPlabels,
                  'values': Dest_IPvalues,
                  'type': 'pie'}],
        'layout': {'title': 'Destination IP vs # of packets'}
         }

    py.offline.plot(figB)

def Protocol():
    figC = {
        'data': [{'labels': Protocollabels,
                  'values': Protocolvalues,
                  'type': 'pie'}],
        'layout': {'title': 'Protocol usage by %'}
         }

    py.offline.plot(figC)

def src_Port():
    figD = {
        'data': [{'labels': Src_Portlabels,
                  'values': Src_Portvalues,
                  'type': 'pie'}],
        'layout': {'title': 'Source Port vs # of packets'}
         }

    py.offline.plot(figD)

def dest_Port():
    figE = {
        'data': [{'labels': Dest_Portlabels,
                  'values': Dest_Portvalues,
                  'type': 'pie'}],
        'layout': {'title': 'Destination Port vs # of packets'}
         }

    py.offline.plot(figE)

def ttl():
    figF = {
        'data': [{'labels': ttl_labels,
                  'values': ttl_values,
                  'type': 'pie'}],
        'layout': {'title': 'TTL of packets'}
         }

    py.offline.plot(figF)

def pretty_picture():
    cont = True
    while cont:
        choice = str(raw_input("What Would You Like To See? Press ? to see choices or quit to exit: ")).lower()

        if choice == '?':
            print "Your Pie Chart Examples Include:\n" \
                  "Source IP vs # of packets: Src IP \n" \
                  "Destination IP vs # of packets: Dest IP \n" \
                  "Source Port vs # of packets: Src Port\n" \
                  "Destination Port vs # of packets: Dest Port\n" \
                  "Protocol used: Protocol\n" \
                  "Time to Live: ttl\n" \
                  "To exit the program: Quit"

        elif choice == "src ip":
            src_IP()
        elif choice == "dest ip":
            dest_IP()
        elif choice == "src port":
            src_Port()
        elif choice == "dest port":
            dest_Port()
        elif choice == "protocol":
            Protocol()
        elif choice == "ttl":
            ttl()
        elif choice == "quit":
            print "Bye!"
            cont=False
        else:
            print "Incorrect command"

pretty_picture()
