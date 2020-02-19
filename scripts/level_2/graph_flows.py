#!/usr/bin/env python2

import plotly.graph_objects as go
import pandas as pd
import sys

data = pd.read_csv(sys.argv[1])
dataHeader = data.columns.values
data = data.sort_values(dataHeader[1], ascending=False)
fig = go.Figure()
for index, row in data.iterrows():
    fig.add_trace(go.Bar(x=[row[1]], y=[row[0]], name=str(row[3]) + ' ' + dataHeader[3]))
fig.update_layout(xaxis_type='category',
    xaxis_title='protocol', yaxis_title='bytes', xaxis={'categoryorder':'category ascending'})
fig.show()
