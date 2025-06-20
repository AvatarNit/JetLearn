import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson3\titanic.csv")

print(data.info)
print(data.isnull().sum())

data["Age"].fillna(data["Age"].median(skipna=True), inplace= True)

data["Embarked"].fillna(data["Embarked"].value_counts().idxmax(), inplace= True)

print(data.isnull().sum())

data.drop("PassengerId", axis= 1, inplace=True)
data.drop("Name", axis= 1, inplace=True)
data.drop("Cabin", axis= 1, inplace=True)
data.drop("Ticket", axis= 1, inplace=True)

data["TravelAlone"] = np.where((data["SibSp"]+data["Parch"]) > 0, 0, 1)
data.drop("SibSp", axis= 1, inplace=True)
data.drop("Parch", axis= 1, inplace=True)

print(data.head())

# Setting columns to 0 & 1
from sklearn.preprocessing import LabelEncoder
labelEncoder = LabelEncoder()
data["Sex"] = labelEncoder.fit_transform(data["Sex"])
data["Embarked"] = labelEncoder.fit_transform(data["Embarked"])

print(data.head())

from sklearn.model_selection import train_test_split
X = data[["Pclass","Sex","Age","Fare","Embarked","TravelAlone"]]
y = data["Survived"]
XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=2)

# Classification: Logistical Regression
from sklearn.linear_model import LogisticRegression
Reg = LogisticRegression()
Reg.fit(XTrain,yTrain)
yPredict = Reg.predict(XTest)

# Confusion Matrix / Error Matrix

from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(yTest,yPredict)
sns.heatmap(matrix,annot=True,fmt="d")

plt.title("Confusion Matrix")
plt.xlabel("Predict")
plt.ylabel("Actual")
plt.show()

# Accuracy
from sklearn.metrics import accuracy_score
print("Acurracy: " , accuracy_score(yTest,yPredict))