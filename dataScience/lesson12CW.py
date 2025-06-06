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