import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson4\iris.csv")

print(data.head())
print(data.info())

X = data[["sepal_length","sepal_width","petal_length","petal_width"]]
y = data["species"]

# Preprocessing
from sklearn.preprocessing import LabelEncoder, StandardScaler
encoder = LabelEncoder()

y = encoder.fit_transform(y)

scaler = StandardScaler()
X = scaler.fit_transform(X)

print(X)
print(y)

from sklearn.model_selection import train_test_split
XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=5)

# KNN Algorithm (K nearest neighbor)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()

classifier.fit(XTrain,yTrain)
yPredict = classifier.predict(XTest)


# Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

sns.heatmap(confusion_matrix(yTest,yPredict),annot=True,fmt="d")

plt.title("Confusion Matrix")
plt.xlabel("Predict")
plt.ylabel("Actual")

plt.show()

# Accuracy
print(f"Accuracy: {accuracy_score(yTest,yPredict)*100}%")


# Classification Report
print("Classification Report:\n" , classification_report(yTest,yPredict))