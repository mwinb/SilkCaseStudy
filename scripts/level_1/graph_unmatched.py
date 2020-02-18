#!/usr/bin/env python2

import plotly.graph_objects as go
import pandas as pd
import sys

data = pd.read_csv(sys.argv[1])
dataHeader = data.columns.values
dataRows = data.loc[:, :][1:]
fig = go.Figure()
for index, row in data.iterrows():
    fig.add_trace(go.Bar(x=[row[1]], y=[row[2]], name=row[0]))
fig.update_layout(xaxis_type='category',
    xaxis_title=dataHeader[1], yaxis_title=dataHeader[2], xaxis={'categoryorder':'category ascending'})
fig.show()
