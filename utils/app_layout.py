from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from utils import yield_curve_plots as ycp


def create_layout(df, source, id_vars, low, high):
    layout = dbc.Container([
        dbc.Row(
            [dbc.Col(

                html.Div(children=[
                    dcc.Graph(id='graph',
                              figure=ycp.plot_historical_yield_curve(df, source_text=source, id_vars=id_vars),
                              style={'width': '100%'},
                              )], ),
                xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4'),
            ], justify='center'),

        # html.Br(),

        dbc.Row([
            dbc.Col(dcc.Graph(id="US",
                              figure=ycp.plot_yield_curve_surface(df,source_text=source),
                              # style={'width': '100%'},
                              # responsive=True,
                              ),
                    xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4'),
        ],
            justify='center',
        ),

        dbc.Row([

            dbc.Col(
                dcc.Graph(figure=ycp.plot_heatmap(df, source_text=source)),
                xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4'),
        ], justify='center'),

        html.Br(),

        dbc.Row([
            dbc.Col(
                dcc.Graph(figure=ycp.plot_line_spread(df, idx=id_vars, low=low, high=high,
                                                      source_text=source)),
                xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4'),
        ], justify='center'),

    ],
        fluid=True,
        class_name="dbc",
        style={
            # "margin-left": "3rem",
            # "margin-right": "3rem",
            "width": "100%",
            # "padding": "2rem 2rem 2rem 2rem",
        }
    )

    return layout
