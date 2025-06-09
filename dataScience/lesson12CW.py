import numpy as np
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\dataScience\lesson12-capstone\IndianHealthyRecipe.csv")

data = data[["Dish Name","Prep Time","Views","Rating"]]

print(data.info())
print(data.describe())
print(data.head())

from sklearn.preprocessing import StandardScaler

Scaler = StandardScaler()

data["Views"] = Scaler.fit_transform(data[["Views"]])
data["Rating"] = Scaler.fit_transform(data[["Rating"]])
print(data.info())
print(data.describe())
print(data.head())

print(set(data["Prep Time"]))

data["Prep Time"] = data["Prep Time"].map({'Prep 25 mins': 25, 'Prep 35 mins':35, 'Prep 5 mins':5, 'Prep 30 mins':30, 'Prep 2 hrs 10 mins':130, 'Prep 12 hrs':720, 'Prep 15 mins':15, 'Prep 20 mins':20, 'Prep 40 mins':40, 'Prep 1 hr 30 mins':90, 'Prep 10 mins':10, 'Prep 2 days':2880})

print("After Map: \n" , set(data["Prep Time"]))

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")

data["Prep Time"] = imputer.fit_transform(data[["Prep Time"]])
print("After Null replacement: \n" , set(data["Prep Time"]))
data["Prep Time"] = Scaler.fit_transform(data[['Prep Time']])
print("After Scaler: \n" , set(data["Prep Time"]))


print(data.info())
print(data.describe())
print(data.head())

topPrepDish10 = data.nlargest(10,"Prep Time")

fig1 = go.Figure()

fig1.add_trace(go.Bar(x=topPrepDish10["Dish Name"], y=topPrepDish10["Prep Time"], marker_color='orange'))
fig1.update_layout(
    title="Top 10 Recipes by Prep Time",
    xaxis_title="Recipes",
    yaxis_title="Preptime"
)

fig1.write_html("fig1.html",auto_open=True)




topViewDish10 = data.nlargest(10,"Views")

fig2 = go.Figure()

fig2.add_trace(go.Bar(x=topViewDish10["Dish Name"], y=topViewDish10["Views"], marker_color='green'))
fig2.update_layout(
    title="Top 10 Recipes by Views",
    xaxis_title="Recipes",
    yaxis_title="Views"
)

fig2.write_html("fig2.html",auto_open=True)



topRatingDish10 = data.nlargest(10,"Rating")

fig3 = go.Figure()

fig3.add_trace(go.Bar(x=topRatingDish10["Dish Name"], y=topRatingDish10["Rating"], marker_color='green'))
fig3.update_layout(
    title="Top 10 Recipes by Rating",
    xaxis_title="Recipes",
    yaxis_title="Rating"
)

fig3.write_html("fig3.html",auto_open=True)



bottomRatingDish10 = data.nsmallest(10,"Rating")

fig4 = go.Figure()

fig4.add_trace(go.Bar(x=bottomRatingDish10["Dish Name"], y=bottomRatingDish10["Rating"], marker_color='red'))
fig4.update_layout(
    title="Bottom 10 Recipes by Rating",
    xaxis_title="Recipes",
    yaxis_title="Rating"
)

fig4.write_html("fig4.html",auto_open=True)
