#!/usr/bin/env python2

import plotly.graph_objects as go
import pandas as pd
import sys

data = pd.read_csv(sys.argv[1])
dataHeader = data.columns.values
dataRows = data.loc[:, :]
fig = go.Figure()
for row in dataRows:
    fig.add_trace(go.Bar(x=row[1], y=row[2], name=row[0]))
fig.update_layout(barmode='stack', xaxis={'categoryorder': 'category'})
fig.show()


# fig = go.Figure(data=[
#     go.Bar(name="unmatched", x=data[dataHeader[0]], y=data[dataHeader[2]]),
# ])
# print(data[dataHeader[0]])
# # Change the bar mode
# fig.update_layout(barmode='group')
# # fig.update_layout(color=inBoundHeader[0])
# fig.update_layout(xaxis_type='category',
#                   xaxis_title=dataHeader[0], yaxis_title=dataHeader[1])
# fig.show()
