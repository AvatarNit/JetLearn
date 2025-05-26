import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\dataScience\lesson10-covid2\WHO-COVID-19-global-data.csv")

data = data[["DateReported","Country","New_cases","Cumulative_cases","New_deaths","Cumulative_deaths"]]

# Convert to pandas date time
print(type(data["DateReported"][0])) # <class 'str'>
data["DateReported"] = pd.to_datetime(data["DateReported"])
print(type(data["DateReported"][0])) # <class 'pandas._libs.tslibs.timestamps.Timestamp'>

dates = data.groupby("DateReported").sum()
print(dates)

fig1 = go.Figure() # Creating the area for the graph

    # Plots a Scatter plot, connects with line, fills below line
fig1.add_trace(go.Scatter(x=dates.index, y=dates["Cumulative_cases"], fill="tonexty",line_color="blue"))

fig1.update_layout(title="Cumulative Cases Worldwide")

fig1.write_html("fig1.html",auto_open=True)


fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=dates.index, y=dates["Cumulative_deaths"], fill="tonexty", line_color="red"))
fig2.update_layout(title="Cumulative Deaths Worldwide")
fig2.write_html("fig2.html",auto_open=True)

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=dates.index, y=dates["New_deaths"], fill="tonexty", line_color="red"))
fig3.update_layout(title="New Deaths Worldwide")
fig3.write_html("fig3.html",auto_open=True)

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=dates.index, y=dates["New_cases"], fill="tonexty", line_color="orange"))
fig4.update_layout(title="New Cases Worldwide")
fig4.write_html("fig4.html",auto_open=True)

