import pandas as pd

df = pd.DataFrame({
    "Name": ["Aang","Katara","Sokka","Toph","a","b","c"],
    "Age": [112,12,15,11,1,2,3],
    "City": ["Southern Air Temple", "Southern Water Tribe","Southern Water Tribe","Earth Kingdom","x","y","z"]
})
# Displays top 5 elements
print(df.head())
# Displays top (x) elements
print(df.head(7))
# Prints dimensions of data set
print(df.shape)
# Prints general info about data set
print(df.info())
# Displays mathematical values on all num columns
print(df.describe())

print(df["Age"][0])
print(df["Age"])

print(df["Age"].max())
print(df["Age"].shape)

data = pd.read_csv("C:/Users/sajja/OneDrive/Desktop/VSCode/dataScience/lesson3-pandas/titanic.csv")
print(data.head())
print(data.shape)
print(data.info())
print(data.describe())

print(data[["Name","Age"]])
print(data[data["Age"] > 35])
print(data[data["Pclass"] == 2])
print(data[(data["Pclass"] == 2) | (data["Pclass"] == 3)])
print(data[data["Pclass"].isin([2,3])])

print(data["Fare"][(data["Sex"] == "male") & (data["Pclass"] == 1)].describe()["mean"])

x = data[(data["Sex"] == "male") & (data["Pclass"] == 1)]
print(x["Fare"].mean())

print(data["Fare"][(data["Sex"] == "female") & (data["Pclass"] == 1)].mean())
print(data["Fare"][(data["Sex"] == "male") & (data["Pclass"] == 2)].mean())
print(data["Fare"][(data["Sex"] == "female") & (data["Pclass"] == 2)].mean())
print(data["Fare"][(data["Sex"] == "male") & (data["Pclass"] == 3)].mean())
print(data["Fare"][(data["Sex"] == "female") & (data["Pclass"] == 3)].mean())
