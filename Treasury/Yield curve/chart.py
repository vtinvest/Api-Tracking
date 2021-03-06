# https://chart-studio.plotly.com/~vkinvest/458/#/

import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objs as go


charts = pd.read_excel('yield curve chart.xlsx').T
charts.columns = charts.T['Date']
charts = charts[1:]

def scatter():
    charts_list = []

    for col in charts.columns:
        charts_bar = go.Scatter(
            name=str(col.strftime("%Y/%m/%d")),
            x=charts.index,
            y=charts[col]
        )
        print(col)
        charts_list.append(charts_bar)
    fig_is = go.Figure(data=charts_list, layout=go.Layout(barmode='stack'))
    py.plot(fig_is, filename='2021 yield curve - Jan')


scatter()