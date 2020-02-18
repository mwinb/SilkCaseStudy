#!/usr/bin/env python2

import plotly.graph_objects as go
import pandas as pd
import sys

data = pd.read_csv(sys.argv[1])
dataHeader = data.columns.values
fig = go.Figure(data=[
    go.Bar(name="unmatched", x=data[dataHeader[1]], y=data[dataHeader[2]]),
])
print(data[dataHeader[0]])
# Change the bar mode
fig.update_layout(barmode='group')
# fig.update_layout(color=inBoundHeader[0])
fig.update_layout(xaxis_type='category',
                  xaxis_title=str(dataHeader[1] + '\' + dataHeader[0]), yaxis_title=dataHeader[1])
fig.show()
