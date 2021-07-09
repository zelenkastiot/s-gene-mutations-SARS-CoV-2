"""

 Created on 01-Jul-21
 @author: Kiril Zelenkovski

"""
import six.moves.urllib.request as urlreq
from six import PY3
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import json
import base64
import os
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bio as dashbio
import os
import glob
import pandas as pd
import collections
import plotly.graph_objs as go

# Read combined_csv_data from 0-phase
df = pd.read_csv("C:\\Users\\zelen\\Desktop\\Sars-Cov-2-variants\\combined_data-2.csv")

# List all lineages
all_lineages = []
for index, row in df.iterrows():
    all_lineages.append(row['#Top Lineage'].split(" ")[1])
    # if row['#Top Lineage'].split(" ")[1] == "B.1.1.70":
    #     print(row['Variant'])

counter = collections.Counter(all_lineages)
c = counter.most_common(5)

labels_full = []
values_full = []
for i in reversed(c):
    label = i[0]
    value = i[1]
    labels_full.append(label)
    values_full.append(value)

figb = go.Figure(data=[
    go.Bar(name='GISAID data',
           x=labels_full,
           y=values_full,
           marker_color="rgb(255, 25, 120)",
           text=values_full,
           textposition='outside',
           texttemplate='%{text}<br> ',
           textfont=dict(
               size=12,
               color="black"),
           hovertemplate="<b> Linage: </b> <i> %{x} </i>, <br><b> # variants: </b> <i> %{y} </i> <br>")
])

figb.update_layout(title='',
                   title_x=0.5,
                   xaxis_title='PANGO lineages',
                   xaxis=dict(range=[-0.45, 4.45],
                              mirror='all',
                              ticks='outside',
                              showline=True,
                              linecolor='#000',
                              tickfont=dict(size=16)),
                   yaxis_title='# of variants with linage',
                   yaxis=dict(range=[0, 3500],
                              mirror=True,
                              ticks='outside',
                              showline=True,
                              linecolor='#000',
                              tickfont=dict(size=16)),
                   plot_bgcolor='#fff',
                   width=950,
                   height=510,
                   font=dict(size=13),
                   margin=go.layout.Margin(l=70,
                                           r=50,
                                           b=70,
                                           t=110),
                   bargap=0.25,
                   bargroupgap=0.1)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = urlreq.urlopen(
    'https://raw.githubusercontent.com/zelenelez/images/master/example2.fasta'
).read()

if PY3:
    data = data.decode('utf-8')

app.layout = html.Div([
    html.Br(),

    html.Center(html.H1('PANGO Linage analysis')),
    html.Center(html.H5('Five most common lineages [July 2020 - June 2021]')),

    html.Br(),
    html.Br(),

    html.Div([
        html.Div([
            html.Center(html.H3('')),
            html.Div([
                dashbio.AlignmentChart(
                    id='my-alignment-viewer',
                    data=data,
                    showgap=False,
                    showconsensus=False,
                    colorscale='hydro',
                    conservationcolorscale='blackbody'
                ),
            ])
        ], className="six columns"),

        html.Div([
            html.Center(html.H3('(b) # of variants with lineage')),
            dcc.Graph(
                id='graph-2',
                figure=figb
            )
        ], className="six columns"),

    ], className="row"),
    html.Div(id='alignment-viewer-output')
])


@app.callback(
    dash.dependencies.Output('alignment-viewer-output', 'children'),
    [dash.dependencies.Input('my-alignment-viewer', 'eventDatum')]
)
def update_output(value):
    if value is None:
        return 'No data.'
    return str(value)


if __name__ == '__main__':
    app.run_server(debug=True)
