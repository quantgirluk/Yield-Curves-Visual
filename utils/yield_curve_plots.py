import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np


def plot_yield_curve_surface(df, source_text):
    radius = 1.95
    first_tenor = df.columns[-1]
    fig = go.Figure(data=[
        go.Surface(x=df.columns,
                   y=df.index,
                   z=df.values,
                   contours={"x": {"show": True, "color": "lightblue", "size": 0.01,
                                   "project": {"x": False, "y": False, "z": False}},
                             "y": {"show": False, "highlight": True},
                             "z": {"show": False, "highlight": False}},
                   # opacity=0.99,
                   connectgaps=False,
                   colorscale='ice',
                   # colorscale=[[1, 'rgb(230, 238, 255)'], [0, 'rgb(0, 32, 102)']],
                   cmin=-2,
                   # cmax=11,
                   showscale=False,
                   reversescale=True,
                    hovertemplate='Maturity: %{x}' +\
                                  '<br>Date: %{y}' +\
                                  '<br>Yield: %{z:.2f}<extra></extra>',
                    # text = [title for title in df.Title],
                   ),
    ]
    )


    fig.update_layout(title='Historical Yield Curve',
                      title_font=dict(size=20),
                      autosize=True,
                      # width=1800,
                      height=900,
                      hovermode='closest',
                      scene={
                          'aspectratio': {"x": 1, "y": 1.75, "z": 0.75},
                          'camera': {
                              'up': {'x': 0, 'y': 0, 'z': 1.0},
                              'eye': {'x': 1.0 * radius, 'y': 0.5 * radius, 'z': 0.35 * radius},
                              'center': {'x': 0., 'y': 0., 'z': -0.1},
                          },
                          'xaxis': {'zeroline': False, "showspikes": False, "showline": False},
                          'yaxis': {'zeroline': False, "showspikes": False, "showline": False},
                          'zaxis': {"showspikes": False},
                          'xaxis_title': '',
                          'yaxis_title': '',
                          'zaxis_title': ''
                      },
                      margin=dict(l=40, r=40, b=40, t=40),
                      annotations=[
                          dict(
                              text=source_text,
                              x=0.0,
                              y=0.0,
                              align="right",
                              xref="paper",
                              yref="paper",
                              showarrow=False
                          )
                      ]
                      )

    # fig.add_scatter3d(x=[first_tenor],
    #                   y=df.index,
    #                   z=df[[first_tenor]].values,
    #                   mode='markers',
    #                   line=dict(
    #                       color='red',
    #                       width=2
    #                   ),
    #                   marker=dict(
    #                       size=2,
    #                       color=df[[first_tenor]].values,
    #                       colorscale='Viridis',
    #                   ),
    #                   )
    # fig.show(config={'modeBarButtonsToRemove': ['zoom', 'pan']})
    return fig


def plot_heatmap(df, source_text):
    data = df.T
    data = data.iloc[::-1]  # to reverse order of rows in a df
    fig = go.Figure(data=[go.Heatmap(z=data.values,
                                     x=data.columns,
                                     y=data.index,
                                     colorscale='ice',
                                     zmin=-2,
                                     showscale=True,
                                     reversescale=True,
                                     hovertemplate='Maturity: %{y}' + \
                                                   '<br>Date: %{x}' + \
                                                   '<br>Yield: %{z:.2f}<extra></extra>',
                                     )])

    fig.update_xaxes(title=None)
    fig.update_layout(title='Yield Curve Heatmap',
                      title_font=dict(size=20),
                      autosize=True,
                      # width=1200,
                      height=500,
                      coloraxis_showscale=False,
                      margin=dict(t=40),
                      annotations=[
                          dict(
                              text=source_text,
                              x=0,
                              y=-0.1,
                              xref="paper",
                              yref="paper",
                              showarrow=False
                          )
                      ]
                      )
    return fig


def plot_historical_yield_curve(df, source_text, id_vars='DATE'):
    df_rev = df.iloc[:, ::-1]
    tabular_df = pd.melt(df_rev.reset_index(), id_vars=id_vars, value_vars=df_rev.columns, var_name='Maturity',
                         value_name='Yield')
    tabular_df[id_vars] = tabular_df[id_vars].dt.strftime('%Y-%m')
    max_yield = tabular_df.Yield.max()
    min_yield = tabular_df.Yield.min()

    fig = px.line(tabular_df,
                  x='Maturity',
                  y='Yield',
                  animation_frame=id_vars,
                  animation_group='Maturity',
                  range_y=[int(min_yield), int(max_yield) + 2],
                  markers='*',
                  # text=tabular_df.Yield,
                  )
    fig.update_traces(mode='markers+text',
                      textposition='top center',
                      textfont=dict(
                          family='Arial',
                          size=14,
                      )
                      )

    fig.update_layout(title='Monthly Yield Curve',
                      title_font=dict(size=20),
                      autosize=True,
                      # width=100,
                      height=600,
                      # annotations=[
                      #     dict(
                      #         text=source_text,
                      #         x=0,
                      #         y=-0.15,
                      #         xref="paper",
                      #         yref="paper",
                      #         showarrow=False
                      #     )
                      # ]
                      )
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 100
    # fig.show(animation=dict(fromcurrent=True,mode='immediate'))
    # Auto-play animation
    # plotly.offline.plot(fig, auto_play = True)
    return fig


def plot_line_spread(df, idx, low, high, source_text):
    data = df.copy()
    data['Spread'] = (df[high] - df[low])
    # data['Inverted'] = np.where(data['Spread'] < 0, 1, 0)
    mask = data['Spread'] <= 0
    data['Spread_above'] = np.where(mask, data['Spread'], 0)
    data['Spread_below'] = np.where(mask, 0, data['Spread'])
    fig = px.area(data.reset_index(),
                  x=idx,
                  y='Spread',
                  # color='Inverted',
                  # color_discrete_map={
                  #     'positive': 'steelblue',
                  #     'negative': 'crimson'
                  # },
                  )
    fig.add_trace(go.Scatter(x=data.index, y=data['Spread_above'], fill='tozeroy', mode='none'))
    fig.add_trace(go.Scatter(x=data.index, y=data['Spread_below'], fill='tozeroy', mode='none'))

    fig.update_xaxes(title=None)

    fig.update_layout(title=f'Spread % between the {high} and the {low} rates',
                      title_font=dict(size=20),
                      autosize=True,
                      # width=1000,
                      # height=800,
                      margin=dict(t=40),
                      annotations=[dict(text=source_text, x=0, y=-0.1, xref="paper",
                                        yref="paper",
                                        showarrow=False
                                        )
                                   ]

                      )
    return fig
