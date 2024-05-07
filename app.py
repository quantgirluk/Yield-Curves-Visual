import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from dash_bootstrap_templates import load_figure_template

from utils.styles import CONTENT_INTRO

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css"
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.SPACELAB, dbc_css],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width,initial-scale=1.0'}],
                use_pages=True,
                )
server = app.server
load_figure_template("lux")

title = html.H1(children="Yield Curves Visualization",
                className='text-center mt-4',
                style={'fontSize': 30})

# Modal
with open("learn_more.md", "r") as f:
    howto_md = f.read()

modal_overlay = dbc.Modal(
    [
        dbc.ModalBody(html.Div([dcc.Markdown(howto_md)], id="howto-md")),
        dbc.ModalFooter(dbc.Button("Close", id="howto-close", className="howto-bn")),
    ],
    id="modal",
    size="lg",
)

button_howto = dbc.Button(
    "Learn More",
    id="howto-open",
    outline=True,
    color="info",
    # Turn off lowercase transformation for class .button in stylesheet
    style={"textTransform": "none"},
)

button_github = dbc.Button(
    "GitHub Repository",
    outline=True,
    color="primary",
    href="https://github.com/quantgirluk/Yield-Curves-Visual",
    id="gh-link",
    style={"text-transform": "none"},
)

# Header
header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        # html.Img(
                        #     id="logo",
                        #     src=app.get_asset_url("dash-logo-new.png"),
                        #     height="30px",
                        # ),
                        # md="auto",
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.H4("Yield Curves Visualisation"),
                                    html.P(dcc.Markdown("By [Dialid Santiago](https://quantgirl.blog)"))
                                ],
                                id="app-title",
                            )
                        ],
                        md="auto",
                        align="center",
                    ),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.NavbarToggler(id="navbar-toggler"),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavItem(button_howto),
                                        dbc.NavItem(button_github),
                                    ],
                                    navbar=True,
                                ),
                                id="navbar-collapse",
                                navbar=True,
                            ),
                            modal_overlay,
                        ],
                        # md=2,
                    ),
                ],
                align="center",
            ),
        ],
        fluid=True,
    ),
    dark=False,
    # color="dark",
    # sticky="top",
)

# Description
description = dbc.Col(
    [
        dbc.Card(
            id="description-card",
            children=[
                dbc.CardHeader("Explanation"),
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Img(
                                            src="assets/segmentation_img_example_marks.jpg",
                                            width="200px",
                                        )
                                    ],
                                    md="auto",
                                ),
                                dbc.Col(
                                    html.P(
                                        "This is an example of interactive machine learning for image classification. "
                                        "To train the classifier, draw some marks on the picture using different "
                                        "colors for "
                                        'different parts, like in the example image. Then enable "Show segmentation" '
                                        'to see the '
                                        "classes a Random Forest Classifier gave to regions of the image, based on the "
                                        "marks you "
                                        "used as a guide. You may add more marks to clarify parts of the image where "
                                        "the "
                                        "classifier was not successful and the classification will update."
                                    ),
                                    md=True,
                                ),
                            ]
                        ),
                    ]
                ),
            ],
        )
    ],
    md=12,
)

app.layout = html.Div(children=[

    header,

    dbc.Container(
        dbc.Row([html.Div(id='yield-curve-101',
                          children=[
                              dcc.Markdown('''            
                  --- 
                                                                                                             
                  **Yield Curve 101**  
                  
                  The yield curve shows how much it costs the federal 
                  government to borrow money 
                  for a given amount of time, revealing the relationship between long- and short-term 
                  interest rates. 
                  
                  It is, inherently, a forecast for what the economy holds in the 
                  future — how much inflation there will be, for example, and how healthy growth will 
                  be over the years ahead — all embodied in the price of money today, tomorrow and 
                  many years from now.  
                  
                  — *The New York Times (2015)*.
                  
                  --- 
                ''')
                          ],
                          className='text-justify mt-4', style={'fontSize': 15})
                 ]),

        fluid=True,
        style={
            # "margin-left": "3rem",
            # "margin-right": "3rem",
            "width": "70%",
            # "padding": "2rem 2rem 2rem 2rem",
        },
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
              If you like this project, please give it a star
               in [GitHub](https://github.com/quantgirluk/Yield-Curves-Visual) ⭐️
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
                                            
                                            Hello, my name is [Dialid](https://quantgirl.blog/about-me/). I am a 
                                            Mathematician and a Finance Quantitative Analyst based in London. I create 
                                            open source projects and write about financial mathematics, programming, 
                                            statistics, data visualisation, and related topics.
                                            
                                            I have over 8 years of experience working as a Quant. Currently, I am 
                                            working in the Cross-Asset front office quant team at Bank of America. 
                                            My previous experience includes the development and implementation of 
                                            mathematical models for Counterparty Credit Risk, Market Risk, and Wholesale 
                                            Credit Risk, as well as Validation in Retail Credit Risk. 
                                            
                                            I hold a PhD in Mathematics/Statistics from the University of Warwick where 
                                            I spent 4 amazing years focusing on non-linear stochastic processes. 
                                            Before coming to the UK, I obtained an MSc in Probability and Statistics, 
                                            and a BSc in Applied Mathematics in Mexico. 
                                            
                                            I regularly write about diverse topics [here](https://quantgirl.blog).
                                            
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
            "width": "70%",
            # "padding": "2rem 2rem 2rem 2rem",
        },
        class_name="dbc"
    ),
])


# Callback for modal popup
@app.callback(
    Output("modal", "is_open"),
    [Input("howto-open", "n_clicks"), Input("howto-close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == '__main__':
    server = app.server
app.run_server(debug=True,
               host='0.0.0.0',
               port=10000
               )
