#!/usr/bin/env python2
import pandas as pd
import plotly.express as px
import sys

df = pd.read_csv(sys.argv[1])
headerList = df.columns.values
print headerList
fig = px.bar(df, x=range(len(df)), y=headerList[1], color=headerList[0])
fig.show()
