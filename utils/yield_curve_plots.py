import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def plot_yield_curve_surface(df):
    fig = go.Figure(data=[go.Surface(x=df.columns,
                                     y=df.index,
                                     z=df.values,
                                     opacity=0.95,
                                     connectgaps=True,
                                     colorscale='ice',
                                     showscale=False,
                                     reversescale=True,
                                     )
                          ]
                    )

    fig.update_layout(title='Yield Curve Historical Evolution',
                      title_font=dict(size=20),
                      autosize=True,
                      # width=1800,
                      height=900,
                      hovermode='closest',
                      scene={'aspectratio': {"x": 1, "y": 2.5, "z": 1},
                             # 'camera': {'eye': {'x': 2, 'y': 0.4, 'z': 0.8}},
                             # 'xaxis': {'title': 'Year', 'showgrid': False, 'zeroline': False},
                             'xaxis_showspikes': False,
                             'yaxis_showspikes': False,
                             'xaxis_title': '',
                             'yaxis_title': '',
                             'zaxis_title': ''
                             },
                      # margin=dict(t=40),
                      margin=dict(
                          r=20, l=20,
                          b=20, t=40),
                      annotations=[
                          dict(
                              text="Data Source: FRED - Federal Reserve Economic Data",
                              x=0,
                              y=-0.15,
                              xref="paper",
                              yref="paper",
                              showarrow=False
                          )
                      ]

                      )
    fig.update_scenes(xaxis_showspikes=False, yaxis_showspikes=False, zaxis_showspikes=False)

    return fig


def plot_heatmap(df):
    data = df.T
    data = data.iloc[::-1]  # to reverse order of rows in a df

    fig = go.Figure(data=[go.Heatmap(z=data.values,
                                     x=data.columns,
                                     y=data.index,
                                     colorscale='ice',
                                     showscale=True,
                                     reversescale=True,
                                     )])

    fig.update_xaxes(title=None)

    fig.update_layout(title='Yield Curve Heatmap',
                      title_font=dict(size=20),
                      autosize=True,
                      # width=1200,
                      height=500,
                      coloraxis_showscale=False,
                      margin=dict(t=38),
                      annotations=[
                          dict(
                              text="Data Source: FRED - Federal Reserve Economic Data",
                              x=0,
                              y=-0.15,
                              xref="paper",
                              yref="paper",
                              showarrow=False
                          )
                      ]
                      )
    return fig


def plot_line_spread(df):
    data = df.copy()
    data['Spread'] = (df['10Y'] - df['3M']) * 100

    fig = px.area(data.reset_index(),
                  x='DATE',
                  y='Spread',
                  range_y=[-200, 400]

                  )
    fig.update_xaxes(title=None)

    fig.update_layout(title='10Y-1M Spread in bps',
                      title_font=dict(size=20),
                      autosize=True,
                      # width=1200,
                      height=500,
                      margin=dict(t=40),
                      annotations=[
                          dict(
                              text="Data Source: FRED - Federal Reserve Economic Data",
                              x=0,
                              y=-0.15,
                              xref="paper",
                              yref="paper",
                              showarrow=False
                          )
                      ]

                      )
    return fig


def plot_historical_yield_curve(df):

    df_rev = df.iloc[:, ::-1]
    tabular_df = pd.melt(df_rev.reset_index(), id_vars='DATE', value_vars=df_rev.columns, var_name='Maturity',
                         value_name='Yield')
    tabular_df['DATE'] = tabular_df['DATE'].dt.strftime('%Y-%m')

    fig = px.line(tabular_df,
                  x='Maturity',
                  y='Yield',
                  animation_frame='DATE',
                  animation_group='Maturity',
                  range_y=[0, 18],
                  markers='*',
                  text=tabular_df.Yield,
                  )
    fig.update_traces(mode='markers+text',
                      textposition='top center',
                      textfont=dict(
                          family='Arial',
                          size=14,
                      )
                      )
    fig.update_xaxes(title=None)
    fig.update_layout(title='Yield Curve Monthly Replay',
                      title_font=dict(size=20),
                      autosize=True,
                      # width=1200,
                      height=500,
                      annotations=[
                          dict(
                              text="Data Source: FRED - Federal Reserve Economic Data",
                              x=0,
                              y=-0.15,
                              xref="paper",
                              yref="paper",
                              showarrow=False
                          )
                      ]
                      )
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 100
    # fig.show(animation=dict(fromcurrent=True,mode='immediate'))
    # Auto-play animation
    # plotly.offline.plot(fig, auto_play = True)
    return fig
