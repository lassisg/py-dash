# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
# import pandas as pd
# from flask import Flask, render_template
# from flaskwebgui import FlaskUI  # get the FlaskUI class

# server = Flask(__name__)
# ui = FlaskUI(server, maximized=True)


# @server.route('/')
# def index():
#     return render_template("index.html",
#                            message="Hello Python+Flask MPT!",
#                            contacts=['c1',
#                                      'c2',
#                                      'c3',
#                                      'c4',
#                                      'c5'])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# 'routes_pathname_prefix' may be '/results/' or '/dash/'
app = dash.Dash(
    __name__,
    # server=server,
    routes_pathname_prefix='/',
    external_stylesheets=external_stylesheets
)

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),

    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),

    html.Label('Text Input'),
    dcc.Input(value='MTL', type='text'),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i)
               for i in range(1, 6)},
        value=5,
    ),
], style={'columnCount': 2})

if __name__ == '__main__':
    # call the 'run' method
    # ui.run()
    app.run_server(debug=True)
