import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson5\car.csv")
data.columns = ("sales","maintainence","doors","persons","boot_space","safety","class")

print(data.head())
print(data.info())

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

data["sales"] = encoder.fit_transform(data["sales"])
data["maintainence"] = encoder.fit_transform(data["maintainence"])
data["doors"] = encoder.fit_transform(data["doors"])
data["persons"] = encoder.fit_transform(data["persons"])
data["boot_space"] = encoder.fit_transform(data["boot_space"])
data["safety"] = encoder.fit_transform(data["safety"])
data["class"] = encoder.fit_transform(data["class"])

print(data.head())
print(data.info())

X = data[["sales","maintainence","doors","persons","boot_space","safety"]]
y = data["class"]

from sklearn.model_selection import train_test_split
XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=2)

# Classification: Decision Tree

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()

classifier = classifier.fit(XTrain,yTrain)

yPredict = classifier.predict(XTest)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

sns.heatmap(confusion_matrix(yTest,yPredict),annot=True,fmt="d")
plt.title(f"Confusion Matrix (Accuracy: {round(accuracy_score(yTest,yPredict)*100,2)}%)")
plt.xlabel("Predict")
plt.ylabel("Actual")

plt.show()

print("Classification Report:\n" , classification_report(yTest,yPredict))