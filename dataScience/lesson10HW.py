import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\dataScience\lesson10-covid2\WHO-COVID-19-global-data.csv")

data = data[["DateReported","Country","New_cases","Cumulative_cases","New_deaths","Cumulative_deaths"]]

userCountry = input("Country: ")
data = data[data["Country"] == userCountry]
data["DateReported"] = pd.to_datetime(data["DateReported"])

print(data)

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=data["DateReported"], y=data["Cumulative_cases"], fill="tonexty", line_color="blue"))
fig1.update_layout(title=f"Cases {userCountry}")
fig1.write_html("fig1.html",auto_open=True)

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=data["DateReported"], y=data["Cumulative_deaths"], fill="tonexty", line_color="red"))
fig2.update_layout(title=f"Deaths {userCountry}")
fig2.write_html("fig2.html",auto_open=True)

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=data["DateReported"], y=data["New_deaths"], fill="tonexty", line_color="pink"))
fig3.update_layout(title=f"New Deaths {userCountry}")
fig3.write_html("fig3.html",auto_open=True)

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=data["DateReported"], y=data["New_cases"], fill="tonexty", line_color="orange"))
fig4.update_layout(title=f"New Cases {userCountry}")
fig4.write_html("fig4.html",auto_open=True)
