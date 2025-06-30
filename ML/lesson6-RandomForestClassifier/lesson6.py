import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson6-RandomForestClassifier\student-mat.csv")

print(data.head())
print(data.info())

data.drop("G1",axis=1,inplace=True)
data.drop("G2",axis=1,inplace=True)
data.drop("address",axis=1,inplace=True)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

data["school"] = encoder.fit_transform(data["school"])
data["sex"] = encoder.fit_transform(data["sex"])
data["famsize"] = encoder.fit_transform(data["famsize"])
data["Pstatus"] = encoder.fit_transform(data["Pstatus"])
data["Mjob"] = encoder.fit_transform(data["Mjob"])
data["Fjob"] = encoder.fit_transform(data["Fjob"])
data["reason"] = encoder.fit_transform(data["reason"])
data["guardian"] = encoder.fit_transform(data["guardian"])
data["schoolsup"] = encoder.fit_transform(data["schoolsup"])
data["famsup"] = encoder.fit_transform(data["famsup"])
data["paid"] = encoder.fit_transform(data["paid"])
data["activities"] = encoder.fit_transform(data["activities"])
data["nursery"] = encoder.fit_transform(data["nursery"])
data["higher"] = encoder.fit_transform(data["higher"])
data["internet"] = encoder.fit_transform(data["internet"])
data["romantic"] = encoder.fit_transform(data["romantic"])

print(data.head())
print(data.info())

y = data["G3"]
data.drop("G3",axis=1,inplace=True)
X = data

from sklearn.model_selection import train_test_split
XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=2)


# Classification: Random Forest
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100)

classifier.fit(XTrain,yTrain)
yPredict = classifier.predict(XTest)


from sklearn.metrics import confusion_matrix,accuracy_score

sns.heatmap(confusion_matrix(yTest,yPredict),annot=True,fmt="d")

plt.title(f"Confusion Matrix ({round(accuracy_score(yTest,yPredict)*100,2)}%)")
plt.xlabel("Predict")
plt.ylabel("Actual")

plt.show()