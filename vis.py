"""
Zachary Anthony
Pandas framework visualization
"""

import sqlite3
import pandas
import plotly
import init_db
from plotly.graph_objs import *
from plotly.offline import offline, init_notebook_mode, plot, iplot


#offline.init_notebook_mode(connected=True)

def pretty_picture():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT Number, Src_MAC, Dest_MAC, Src_IP, Src_Port, Dest_IP, Dest_Port, Protocol FROM Store""")
    rows = cursor.fetchall()
    print rows
    '''
    pandas_frame = pandas.DataFrame([[ij for ij in i] for i in rows])
    pandas_frame.rename(columns={0: 'Number', 1: 'Src_MAC', 2: 'Dest_MAC', 3: 'Src_IP', 4: 'Dest_IP', 5: 'Src_Port', 6: 'Dest_port', 7: 'Protocol'}, inplace=True);

    pandas_frame.sort(['Number'], ascending=[1]);

    trace1 = Scatter(
        x=pandas_frame['Src_MAC'],
        y=pandas_frame['Protocol'],
        text='country_names',
        mode='markers'
    )
    layout = Layout(
        xaxis=XAxis(title='Life Expectancy'),
        yaxis=YAxis(type='log', title='GNP')
    )
    data = Data([trace1])
    fig = Figure(data=data, layout=layout)
    plotly.offline.iplot(fig, filename='test')
    '''

pretty_picture()



