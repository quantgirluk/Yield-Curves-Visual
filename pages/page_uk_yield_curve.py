import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

from utils import data_source as ds
from utils import yield_curve_plots as ycp
from utils.styles import CONTENT_STYLE

dash.register_page(__name__, name='UK BoE Yield Curve')

source = "Data Source: Bank of England"
uk_df = ds.get_uk_yield_curve_data()
as_of_date = uk_df.index[-1].strftime("%b-%Y")

# load_figure_template("lux")

as_of_date_component = html.Em(children=f'Data as of {as_of_date}', className='text-center')
layout = dbc.Container(
    [

        # dbc.Row(as_of_date_component, class_name='mt-4'),
        dbc.Row([dbc.Col(dcc.Graph(id="UK", figure=ycp.plot_yield_curve_surface(uk_df, source_text=source)),
                         xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-5'),

                 dbc.Col(dcc.Graph(figure=ycp.plot_heatmap(uk_df, source_text=source)),
                         xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4')
                 ]),

        html.Br(),

        html.Div(
            dbc.Row(
                [dbc.Col(

                    dcc.Graph(id='graph',
                              figure=ycp.plot_historical_yield_curve(uk_df, source_text=source,
                                                                     id_vars='Date'))),

                    # align="center",
                    # xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4'

                ],
                # align="center",
                justify='center'
            )),

        html.Br(),

        dbc.Row(

            dbc.Col(
                dcc.Graph(figure=ycp.plot_line_spread(uk_df, source_text=source, idx='Date', low='2Y', high='10Y')),

                xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4'),
            align="center",
        ),

    ],
    fluid=True,
    style=CONTENT_STYLE,
    class_name="dbc"
)
