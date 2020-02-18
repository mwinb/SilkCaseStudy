#!/usr/bin/env python2

import plotly.graph_objects as go
import pandas as pd
import sys

inbound = pd.read_csv(sys.argv[1])
inBoundHeader = inbound.columns.values
fig = go.Figure(data=[
    go.Bar(name="inbound", x=inbound[inBoundHeader[0]], y=inbound[inBoundHeader[1]]),
])
# Change the bar mode
fig.update_layout(barmode='group')
# fig.update_layout(color=inBoundHeader[0])
fig.update_layout(xaxis_type='category', xaxis_title=inBoundHeader[0], yaxis_title=inBoundHeader[1])
fig.show()
