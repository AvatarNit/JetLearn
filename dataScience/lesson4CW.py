import pandas as pd

data = pd.read_csv("C:/Users/sajja/OneDrive/Desktop/VSCode/dataScience/lesson4-pandas2/titanic.csv")

adult_names = data.loc[data["Age"]>18,"Name"]
print(adult_names)

# Slicing
print(data.iloc[0:5,1:5])

# Setting values
# data.iloc[0:11,2:3] = "Nithik"

print(data.head(10))
data.to_csv("titanic.csv")

# Creating new column
data["updatedFare"] = data["Fare"] + 10
print(data.head())

data["classFare"] = data["Pclass"] * data["Fare"]
print(data.head())

data = data.rename(
    columns= {
        "Pclass": "Class",
        "Survived": "Alive"
    }
)
print(data.head())

ageMean = data["Age"].mean()
fareMean = data["Fare"].mean()
print(ageMean)
print(fareMean)

print((data["Age"] + data["Fare"]).mean())
print(data[["Age","Fare"]].mean())

# Find specific math operations
print(data.agg({
    "Age": ["min","max","median"],
    "Fare": ["min","max"]
}))

# Grouping by 1 column
print(data[["Sex","Age"]].groupby("Sex").mean())
print(data.groupby("Sex")["Age"].mean())

# Grouping by more than 1 column
print(data.groupby(["Sex","Class"])["Fare"].mean())

# number of unique values
print(data["Class"].value_counts())

# Sort acending
a = data.sort_values(by="Age")
print(a[["Name","Age"]])

# Sort decending
b = data.sort_values(by="Age",ascending=False)
print(b[["Name","Age"]])

data["LowerName"] = data["Name"].str.lower()
print(data.head())

# replace values
data["Gender"] = data["Sex"].replace({
    "male" : "M",
    "female" : "F"
})
print(data.head())