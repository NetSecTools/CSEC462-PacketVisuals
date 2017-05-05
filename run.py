import plotly
from plotly.graph_objs import Scatter, Layout
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
        'layout': {'title': 'Source IP vs # of packets'}
         }

    py.offline.plot(figC)

def src_Port():
    figD = {
        'data': [{'labels': Src_Portlabels,
                  'values': Src_Portvalues,
                  'type': 'pie'}],
        'layout': {'title': 'Source IP vs # of packets'}
         }

    py.offline.plot(figD)

def dest_Port():
    figE = {
        'data': [{'labels': Dest_Portlabels,
                  'values': Dest_Portvalues,
                  'type': 'pie'}],
        'layout': {'title': 'Source IP vs # of packets'}
         }

    py.offline.plot(figE)


dest_Port()





