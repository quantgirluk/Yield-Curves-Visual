import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

from utils import data_source as ds
from utils import yield_curve_plots as ycp
from utils.styles import CONTENT_STYLE

dash.register_page(__name__, path='/', name='US Treasuries Yield Curve')

source = "Data Source: FRED - Federal Reserve Economic Data"
df = ds.get_us_yield_curve_data()
as_of_date = df.index[-1].strftime("%b-%Y")

load_figure_template("lux")

as_of_date_component = html.Em(children=f'Data as of {as_of_date}',
                               className='text-center')

layout = dbc.Container([

    # dbc.Row(as_of_date_component,
    #         class_name='mt-4'
    #         ),

    dbc.Row([
        dbc.Col(dcc.Graph(id="US", figure=ycp.plot_yield_curve_surface(df,
                                                                       source_text=source)),
                xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4'),
        dbc.Col(
            dcc.Graph(figure=ycp.plot_heatmap(df, source_text=source)),
            xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4'
        )
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='graph', figure=ycp.plot_historical_yield_curve(df, source_text=source)),
            xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4'),
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col(
            dcc.Graph(figure=ycp.plot_line_spread(df, idx='DATE', low='2-year', high='10-year',
                                                  source_text=source)),
            xs=12, sm=12, md=12, lg=12, xl=12, xxl=6, class_name='mt-4')
    ]),

],

    fluid=True,
    style=CONTENT_STYLE,
    class_name="dbc"
)
