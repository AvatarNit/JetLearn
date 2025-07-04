from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cancerData = datasets.load_breast_cancer()

print(cancerData.keys())
data = pd.DataFrame(cancerData.data)
data.columns = cancerData.feature_names
data["isCancer"] = cancerData.target

print(data.head())
print(data.info())

y = data["isCancer"]
data.drop("isCancer",axis=1)
X = data

XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=50)

# SVM - Support Vector Machine
machine = svm.SVC(kernel="linear") #SVC - Support Vector Classifier
machine.fit(XTrain,yTrain)
yPredict = machine.predict(XTest)


sns.heatmap(metrics.confusion_matrix(yTest,yPredict),fmt="d",annot=True)

plt.title(f"Confusion Matrix (Accuracy: {round(metrics.accuracy_score(yTest,yPredict)*100,2)}%)")
plt.xlabel("Predict")
plt.ylabel("Actual")

plt.show()

print(metrics.classification_report(yTest,yPredict))