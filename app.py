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
from utils.styles import CONTENT_STYLE, CONTENT_INTRO

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
                style={'fontSize': 30})

app.layout = html.Div(children=[
    dbc.Row(title),

    # dbc.Row(
    #     dbc.Container([
    #         dbc.Row(
    #             [
    #                 html.H1("test")
    #             ], justify="center", align="center", className="h-50"
    #         )
    #     ], style={"height": "100vh"}
    #
    #     )
    # ),

    dbc.Container(
        dbc.Row([html.Div(id='text-container',
                          children=[dcc.Markdown('''
                  The yield curve shows how much it costs the federal 
                  government to borrow money 
                  for a given amount of time, revealing the relationship between long- and short-term 
                  interest rates. It is, inherently, a forecast for what the economy holds in the 
                  future — how much inflation there will be, for example, and how healthy growth will 
                  be over the years ahead — all embodied in the price of money today, tomorrow and 
                  many years from now.
                  ''')
                                    ],
                          className='text-justify mt-4 mb-4', style={'fontSize': 15})
                 ]),

        fluid=True,
        style=CONTENT_INTRO,
        class_name="dbc"
    ),

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
        spinner_style={"width": "3rem", "height": "3rem"}),

    html.Br(),

    dbc.Container(
        dbc.Row([html.Div(id='text-container1',
                          children=[dcc.Markdown('''
              If you like this project, please give it a star in [GitHub](https://github.com/quantgirluk/Understanding-Quantitative-Finance) ⭐️
              ''')
                                    ],
                          className='text-center mt-4', style={'fontSize': 15})
                 ]),

        fluid=True,
        style=CONTENT_INTRO,
        class_name="dbc"
    ),



    dbc.Container(
        dbc.Row([html.Div(id='about-me',
                          children=[
                              dcc.Markdown('''
                                            ---                                                                      
                                            ### About Me
                                            
                                            I have 8 years of experience working as a Quant. Currently, I am working in the Cross-Asset front office quant team at Bank of America. My previous experience includes the development and implementation of mathematical models for Counterparty Credit Risk, Market Risk, and Wholesale Credit Risk, as well as Validation in Retail Credit Risk. 
                                            
                                            I hold a PhD in Mathematics/Statistics from the University of Warwick where I spent 4 amazing years focusing on non-linear stochastic processes. Before coming to the UK, I obtained an MSc in Probability and Statistics, and a BSc in Applied Mathematics in Mexico. 
                                            
                                            I regularly write [here](https://quantgirl.blog) about diverse topics.
                                            
                                            Connect with me via:
                                            
                                            - 🦜 [Twitter](https://twitter.com/Quant_Girl)
                                            - 👩🏽‍💼 [Linkedin](https://www.linkedin.com/in/dialidsantiago/)
                                            - 📸 [Instagram](https://www.instagram.com/quant_girl/)
                                            - 👾 [Personal Website](https://quantgirl.blog)
                                            
                                            Thanks for visiting ✨
                                                          ''')
                          ],
                          className='text-justify mt-4 mb-4', style={'fontSize': 15})
                 ]),

        fluid=True,
        style={
            # "margin-left": "3rem",
            # "margin-right": "3rem",
            "width": "85%",
            # "padding": "2rem 2rem 2rem 2rem",
        },
        class_name="dbc"
    ),
])

# app.layout = layout

####################################
# RUN the app
####################################
if __name__ == '__main__':
    server = app.server
app.run_server(debug=True)
