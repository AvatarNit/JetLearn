from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data  = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson7-SVM\heart.csv")

print(data.head())
print(data.info())

X = data[["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]]
y = data["target"]

XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=2)

machine = svm.SVC(kernel="linear")
machine.fit(XTrain,yTrain)
yPredict = machine.predict(XTest)


sns.heatmap(metrics.confusion_matrix(yTest,yPredict),fmt="d",annot=True)
plt.title(f"Confusion Matrix (Accuracy: {round(metrics.accuracy_score(yTest,yPredict)*100,2)}%)")
plt.xlabel("Predict")
plt.ylabel("Actual")

plt.show()

print(metrics.classification_report(yTest,yPredict))
