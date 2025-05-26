import pandas as pd
import matplotlib as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\dataScience\lesson9-CovidAnalysis\covid_data.csv")

print(data.head())
print(data.info())

data = data[["Province_State","Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]

print(data.head())
print(data.info())

data.columns = ("State","Country","LastUpdate","Lat","Long","Confirmed","Recovered","Deaths","Active")

data["State"].fillna(value=" ", inplace=True)

top10_Confirmed = pd.DataFrame(data.groupby("Country") ["Confirmed"].sum().nlargest(10).sort_values(ascending=False))
print(top10_Confirmed.index) # Prints Country names

fig1 = px.scatter(top10_Confirmed, x=top10_Confirmed.index, y="Confirmed", size="Confirmed",size_max=120,color=top10_Confirmed.index,title="Top 10 Countries with Confirmed Cases")

fig1.write_html("fig1.html",auto_open=True)

# Top 10 Recovered
top10_Recovered = pd.DataFrame(data.groupby("Country") ["Recovered"].sum().nlargest(10).sort_values(ascending=False))

fig2 = px.scatter(top10_Recovered,x=top10_Recovered.index,y="Recovered", size="Recovered", size_max=120, color=top10_Recovered.index,title="Top 10 Countries with Recovered Cases")

fig2.write_html("fig2.html",auto_open=True)

# Top 10 Deaths
top10_Deaths = pd.DataFrame(data.groupby("Country") ["Deaths"].sum().nlargest(10).sort_values(ascending=False))

fig3 = px.scatter(top10_Deaths,x=top10_Deaths.index,y="Deaths", size="Deaths", size_max=120, color=top10_Deaths.index,title="Top 10 Countries with Deaths Cases")

fig3.write_html("fig3.html",auto_open=True)

# Top 10 Active
top10_Active = pd.DataFrame(data.groupby("Country") ["Active"].sum().nlargest(10).sort_values(ascending=False))

fig4 = px.scatter(top10_Active,x=top10_Active.index,y="Active", size="Active", size_max=120, color=top10_Active.index,title="Top 10 Countries with Active Cases")

fig4.write_html("fig4.html",auto_open=True)


# Bar Graph
top8_Confirmed = pd.DataFrame(data.groupby("Country") ["Confirmed"].sum().nlargest(8).sort_values(ascending=False))

fig5 = px.bar(top8_Confirmed,x="Confirmed",y=top8_Confirmed.index,height=600,color="Confirmed",orientation="h",color_continuous_scale=["deepskyblue","red"], title="Top 8 Confirmed Cases")

fig5.write_html("fig5.html",auto_open=True)

top8_Recovered = pd.DataFrame(data.groupby("Country") ["Recovered"].sum().nlargest(8).sort_values(ascending=False))
fig6 = px.bar(top8_Recovered,x="Recovered",y=top8_Recovered.index,height=600,color="Recovered",orientation="h",color_continuous_scale=["deepskyblue","red"], title="Top 8 Recovered Cases")

fig6.write_html("fig6.html",auto_open=True)

top8_Deaths = pd.DataFrame(data.groupby("Country") ["Deaths"].sum().nlargest(8).sort_values(ascending=False))
fig7 = px.bar(top8_Deaths,x="Deaths",y=top8_Deaths.index,height=600,color="Deaths",orientation="h",color_continuous_scale=["deepskyblue","red"], title="Top 8 Deaths Cases")

fig7.write_html("fig7.html",auto_open=True)

top8_Active = pd.DataFrame(data.groupby("Country") ["Active"].sum().nlargest(8).sort_values(ascending=False))
fig8 = px.bar(top8_Active,x="Active",y=top8_Active.index,height=600,color="Active",orientation="h",color_continuous_scale=["deepskyblue","red"], title="Top 8 Active Cases")

fig8.write_html("fig8.html",auto_open=True)


topstates_brazil = data["Country"] == "Brazil"
topstates_brazil = data[topstates_brazil].nlargest(5,"Confirmed")

fig9 = go.Figure(data = [
    go.Bar(name="Recovered Cases",x=topstates_brazil["State"],y=topstates_brazil["Recovered"]),
    go.Bar(name="Confirmed Cases",x=topstates_brazil["State"],y=topstates_brazil["Confirmed"]),
    go.Bar(name="Death Cases",x=topstates_brazil["State"],y=topstates_brazil["Deaths"])
])

fig9.update_layout(title="Most Affected States in Brazil",barmode="stack",height=600)

fig9.write_html("fig9.html",auto_open=True)



topstates_us = data["Country"] == "US"
topstates_us = data[topstates_us].nlargest(15,"Confirmed")

fig10 = go.Figure(data = [
    go.Bar(name="Recovered Cases",x=topstates_us["State"],y=topstates_us["Recovered"]),
    go.Bar(name="Confirmed Cases",x=topstates_us["State"],y=topstates_us["Confirmed"]),
    go.Bar(name="Death Cases",x=topstates_us["State"],y=topstates_us["Deaths"])
])

fig10.update_layout(title="Most Affected States in US",barmode="stack",height=600)

fig10.write_html("fig10.html",auto_open=True)



topstates_india = data["Country"] == "India"
topstates_india = data[topstates_india].nlargest(5,"Confirmed")

fig11 = go.Figure(data = [
    go.Bar(name="Recovered Cases",x=topstates_india["State"],y=topstates_india["Recovered"]),
    go.Bar(name="Confirmed Cases",x=topstates_india["State"],y=topstates_india["Confirmed"]),
    go.Bar(name="Death Cases",x=topstates_india["State"],y=topstates_india["Deaths"])
])

fig11.update_layout(title="Most Affected States in India",barmode="stack",height=600)

fig11.write_html("fig11.html",auto_open=True)


