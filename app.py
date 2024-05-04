####################################
# IMPORTS
####################################
import pandas as pd
import datetime

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css"
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.SPACELAB, dbc_css],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width,initial-scale=0.8'}],
                use_pages=True,
                )
# server = app.server
load_figure_template("lux")

title = html.H1(children="Yield Curves Visualization",
                className='text-center mt-4',
                style={'fontSize': 26})


app.layout = html.Div(children=[
    dbc.Row(title),
    dbc.Row([html.Div(id='button',
                      children=[dbc.Button(page['name'],
                                           href=page['path'],
                                           outline=True,
                                           color='dark',
                                           className="me-1")
                                for page in dash.page_registry.values()
                                ],
                      className='text-center mt-4 mb-4', style={'fontSize': 10})
             ]),
    # Content page
    dbc.Spinner(
        dash.page_container,
        fullscreen=True,
        show_initially=True,
        delay_hide=600,
        type='grow',
        spinner_style={"width": "3rem", "height": "3rem"})
])

# app.layout = layout

####################################
# RUN the app
####################################
if __name__ == '__main__':
    server = app.server
    app.run_server(debug=True)
