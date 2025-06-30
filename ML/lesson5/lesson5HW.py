import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson5-DecisionTreeClassifier\Employee.csv")

print(data.head())
print(data.info())

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

data["Education"] = encoder.fit_transform(data["Education"])
data["City"] = encoder.fit_transform(data["City"])
data["Gender"] = encoder.fit_transform(data["Gender"])
data["EverBenched"] = encoder.fit_transform(data["EverBenched"])

print("After encoding:")
print(data.head())
print(data.info())

X = data[["Education","JoiningYear","City","PaymentTier","Age","Gender",'EverBenched',"ExperienceInCurrentDomain"]]
y = data["LeaveOrNot"]

from sklearn.model_selection import train_test_split
xTrain,xTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=2)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()

classifier.fit(xTrain,yTrain)
yPredict = classifier.predict(xTest)


from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

sns.heatmap(confusion_matrix(yTest,yPredict),annot=True,fmt="d")
plt.title(f"Confusion Matrix (Accuracy: {round(accuracy_score(yTest,yPredict)*100,2)}%)")
plt.xlabel("Predict")
plt.ylabel("Actual")

plt.show()

print("Classification Report:\n" , classification_report(yTest,yPredict))