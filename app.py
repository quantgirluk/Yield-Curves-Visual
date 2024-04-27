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

dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.LUX, dbc_css],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width,initial-scale=1.0'}],
                use_pages=True,
                )
server = app.server

load_figure_template("lux")

title = html.H1(children="Yield Curves Visualization",
                className=('text-center mt-4'),
                style={'fontSize': 36})


def layout():
    return html.Div(children=[
        dbc.Row(title),
        dbc.Row([html.Div(id='button',
                          children=[dbc.Button(page['name'],
                                               href=page['path'],
                                               outline=True,
                                               color='dark',
                                               className="me-1")
                                    for page in dash.page_registry.values()
                                    ],
                          className=('text-center mt-4 mb-4'), style={'fontSize': 20})
                 ]),
        # Content page
        dbc.Spinner(
            dash.page_container,
            fullscreen=True,
            show_initially=True,
            delay_hide=600,
            type='border',
            spinner_style={"width": "3rem", "height": "3rem"})
    ])


app.layout = layout

### GOOGLE ANALYTICS TAG ###
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        {%favicon%}
        {%css%}
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-K6MBR05TCM"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-K6MBR05TCM');
        </script>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

####################################
# RUN the app
####################################
if __name__ == '__main__':
    server = app.server
    app.run_server(debug=True)
