#!/usr/bin/env python2

import plotly.graph_objects as go
import pandas as pd

inbound = pd.read_csv('inbound.csv')
outbound = pd.read_csv('outbound.csv')
inBoundHeader = inbound.columns.values
outBoundHeader = outbound.columns.values
fig = go.Figure(data=[
    go.Bar(name="inbound", x=inbound[inBoundHeader[0]], y=inbound[inBoundHeader[1]]),
    go.Bar(name="outbound", x=outbound[outBoundHeader[0]], y=outbound[outBoundHeader[1]]),
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.update_layout(xaxis_type='category', xaxis_title=inBoundHeader[0], yaxis_title=outBoundHeader[1])
fig.show()
