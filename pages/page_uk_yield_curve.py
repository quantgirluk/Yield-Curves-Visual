import dash

from utils import data_source as ds
from utils.app_layout import create_layout
from dash_bootstrap_templates import load_figure_template

dash.register_page(__name__, name='UK BoE Yield Curve')

source = "Data Source: Bank of England"
uk_df = ds.get_uk_yield_curve_data()
df = uk_df
id_vars = 'Date'
low = '2Y'
high = '10Y'
load_figure_template("lux")
layout = create_layout(df=df, source=source, id_vars=id_vars, low=low, high=high)
