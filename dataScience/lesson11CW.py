import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\dataScience\lesson11-income\adult.csv")

data.columns = ["age","workclass","id","education","educational-num","marital-status","occupation","relationship","race","gender","capital-gain","capital-loss","hours-per-week","native-country","income"]


data.drop(["age","educational-num","hours-per-week","native-country","id","capital-gain","capital-loss"], axis=1, inplace=True)

data.rename(columns={"marital-status":"marital"},inplace=True)

print(data.describe())
print(data.info())
print(data.isin(["?"]).sum(axis=0))

income = set(data["income"])
print(income)

data["income"] = data["income"].map({" <=50K":0," >50K":1}).astype(int)
print(data.head())

print(set(data["gender"]))
data["gender"] = data["gender"].map({" Male":0," Female":1}).astype(int)

print(data.head())

data.groupby("gender").income.mean().plot(kind="bar")
plt.xlabel("Gender {' Male':0,' Female':1}")
plt.show()

print(set(data["race"]))
data["race"] = data["race"].map({' White':0, ' Black':1, ' Amer-Indian-Eskimo':2, ' Asian-Pac-Islander':3, ' Other':4}).astype(int)
print(data.head())

data.groupby("race").income.mean().plot(kind="bar")
plt.xlabel("Race {' White':0, ' Black':1, ' Amer-Indian-Eskimo':2, ' Asian-Pac-Islander':3, ' Other':4}")
plt.show()


print(set(data['relationship']))
data["relationship"] = data["relationship"].map({' Own-child':0, ' Husband':1, ' Not-in-family':2, ' Unmarried':3, ' Wife':4, ' Other-relative':5}).astype(int)
print(data.head())

data.groupby("relationship").income.mean().plot(kind="bar")
plt.xlabel("Relationship {' Own-child':0, ' Husband':1, ' Not-in-family':2, ' Unmarried':3, ' Wife':4, ' Other-relative':5}")
plt.show()

print(set(data['occupation']))
data["occupation"] = data["occupation"].map({' Tech-support':0, ' Handlers-cleaners':1, ' Other-service':2, ' Prof-specialty':3, ' Sales':4, ' Craft-repair':5, ' ?':6, ' Transport-moving':7, ' Machine-op-inspct':8, ' Exec-managerial':9, ' Adm-clerical':10, ' Priv-house-serv':11, ' Armed-Forces':12, ' Farming-fishing':13, ' Protective-serv':14}).astype(int)
print(data.head())

data.groupby("occupation").income.mean().plot(kind="bar")
plt.xlabel("Occupation {' Tech-support':0, ' Handlers-cleaners':1, ' Other-service':2, ' Prof-specialty':3, ' Sales':4, ' Craft-repair':5, ' ?':6, ' Transport-moving':7, ' Machine-op-inspct':8, ' Exec-managerial':9, ' Adm-clerical':10, ' Priv-house-serv':11, ' Armed-Forces':12, ' Farming-fishing':13, ' Protective-serv':14}")
plt.show()

print(set(data['marital']))
data["marital"] = data["marital"].map({' Never-married':0, ' Separated':1, ' Married-AF-spouse':2, ' Married-spouse-absent':3, ' Married-civ-spouse':4, ' Widowed':5, ' Divorced':6}).astype(int)
print(data.head())

data.groupby("marital").income.mean().plot(kind="bar")
plt.xlabel("Marital {' Never-married':0, ' Separated':1, ' Married-AF-spouse':2, ' Married-spouse-absent':3, ' Married-civ-spouse':4, ' Widowed':5, ' Divorced':6}")
plt.show()


print(set(data['education']))
data["education"] = data["education"].map({' 7th-8th':0, ' Doctorate':1, ' Assoc-acdm':2, ' Prof-school':3, ' 1st-4th':4, ' Some-college':5, ' 5th-6th':6, ' 10th':7, ' HS-grad':8, ' 9th':9, ' Assoc-voc':10, ' 12th':11, ' 11th':12, ' Masters':13, ' Preschool':14, ' Bachelors':15}).astype(int)
print(data.head())

data.groupby("education").income.mean().plot(kind="bar")
plt.xlabel("Education {' 7th-8th':0, ' Doctorate':1, ' Assoc-acdm':2, ' Prof-school':3, ' 1st-4th':4, ' Some-college':5, ' 5th-6th':6, ' 10th':7, ' HS-grad':8, ' 9th':9, ' Assoc-voc':10, ' 12th':11, ' 11th':12, ' Masters':13, ' Preschool':14, ' Bachelors':15}")
plt.show()


print(set(data['workclass']))
data["workclass"] = data["workclass"].map({' Local-gov':0, ' ?':1, ' Self-emp-inc':2, ' Federal-gov':3, ' Without-pay':4, ' Self-emp-not-inc':5, ' Private':6, ' State-gov':7, ' Never-worked':8}).astype(int)
print(data.head())

data.groupby("workclass").income.mean().plot(kind="bar")
plt.xlabel("Workclass {' Local-gov':0, ' ?':1, ' Self-emp-inc':2, ' Federal-gov':3, ' Without-pay':4, ' Self-emp-not-inc':5, ' Private':6, ' State-gov':7, ' Never-worked':8}")
plt.show()