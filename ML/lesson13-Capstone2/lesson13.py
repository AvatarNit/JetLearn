import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson13-Capstone2\Drivers License Data.csv")

print(data.head())
print(data.info())

data.drop("Applicant ID",axis=1,inplace=True)
data.drop("Gender",axis=1,inplace=True)
data.drop("Race",axis=1,inplace=True)

print(data.info())

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

data["Age Group"] = encoder.fit_transform(data["Age Group"])
data["Training"] = encoder.fit_transform(data["Training"])
data["Reactions"] = encoder.fit_transform(data["Reactions"])
data["Qualified"] = encoder.fit_transform(data["Qualified"])

print(data.head())
print(data.info())

y = data["Qualified"]
data.drop("Qualified",axis=1,inplace=True)
X = data

from sklearn.model_selection import train_test_split

XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=2)

from sklearn.metrics import accuracy_score, confusion_matrix

classifierName = []
classifierScore = []
clasifierPredicitions = []


def classify(model,display=False):
    name = (str(type(model)).split(".")[-1]).split("'")[0]
    model.fit(XTrain,yTrain)
    yPredict = model.predict(XTest)
    accuracy = round((accuracy_score(yTest,yPredict)*100),2)

    classifierName.append(name)
    classifierScore.append(accuracy)
    clasifierPredicitions.append(yPredict)

    if display:
        sns.heatmap(confusion_matrix(yTest,yPredict),annot=True,fmt="d")
        plt.title(f"{name} (Accuracy: {accuracy}%)")
        plt.show()
    
    print(f"{name}:{accuracy}%")

def findBest():
    highIndex = 0

    for i in range(1,len(classifierScore)):
        if classifierScore[i] > classifierScore[highIndex]:
            highIndex = i
    
    sns.heatmap(confusion_matrix(yTest,clasifierPredicitions[highIndex]),annot=True,fmt="d")
    plt.title(f"Highest Accuracy Score Model: {classifierName[highIndex]} ({classifierScore[highIndex]}%)")
    plt.show()
    print(f"Highest Accuracy Score:\n\t{classifierName[highIndex]} with {classifierScore[highIndex]}%")


from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Logistic
classify(LogisticRegression())

# KNeighbors
classify(KNeighborsClassifier())

# Decision Tree
classify(DecisionTreeClassifier())

# Random Forest
classify(RandomForestClassifier(n_estimators=100),True)

# SVC
classify(SVC(kernel="poly"))


# Find Highest
findBest()