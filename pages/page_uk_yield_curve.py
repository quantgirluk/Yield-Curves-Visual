import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

from utils import data_source as ds
from utils import yield_curve_plots as ycp

dash.register_page(__name__, name='UK BoE Yield Curve')

source = "Bank of England"
uk_df = ds.get_uk_yield_curve_data()
as_of_date = uk_df.index[-1].strftime("%b-%Y")

# load_figure_template("lux")

as_of_date_component = html.Em(children=f'Data as of {as_of_date}', className='text-center')
layout = dbc.Container([dbc.Row(as_of_date_component, class_name='mb-4'),
                        dbc.Row([
                            dbc.Col(dcc.Graph(id="UK",
                                              figure=ycp.plot_yield_curve_surface(uk_df, source_text=source)),
                                    xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-5'),

                            dbc.Col(
                                dcc.Graph(figure=ycp.plot_heatmap(uk_df, source_text=source)),
                                xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4'
                            )
                        ]),

                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(id='graph', figure=ycp.plot_historical_yield_curve(uk_df, source_text=source,
                                                                                             id_vars='years:')),
                                xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4'),
                            dbc.Col(
                                dcc.Graph(figure=ycp.plot_line_spread(uk_df, source_text=source, idx='years:', low=1,
                                                                      high=10)),
                                xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4')
                        ]),

                        ],
                       fluid=True,
                       class_name="dbc"
                       )
