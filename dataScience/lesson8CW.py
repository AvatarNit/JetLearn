import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\dataScience\lesson8-ML\iris.csv")

# Check if null values present:
print(data.head())
print(data.info())


# Replace with 0,1,2
data["species"] = data["species"].replace({"setosa" : 0, "versicolor" : 1, "virginica" : 2})

# Define input(s) and output
X = data.iloc[:,:-1]
# X = data.drop("species", axis=1)
y = data["species"]

print(X.head())
print(y.head())

# Display data
plt.figure() # Split screen into grid

# sepal_length
plt.subplot(2,2,1) 
plt.scatter(data["sepal_length"], data["species"], s =10, c = "green", marker="o")

# sepal_width
plt.subplot(2,2,2)
plt.scatter(data["sepal_width"], data["species"], s =10, c = "red", marker="o")

# petal_length
plt.subplot(2,2,3)
plt.scatter(data["petal_length"], data["species"], s =10, c = "yellow", marker="o")

# petal_width
plt.subplot(2,2,4)
plt.scatter(data["petal_width"], data["species"], s =10, c = "blue", marker="o")

plt.show()

# Define testing and training data
from sklearn.model_selection import train_test_split

xTrain, xTest, yTrain, yTest = train_test_split(X,y, test_size=0.2, random_state=1)

print(xTrain.shape)
print(xTest.shape)
print(yTrain.shape)
print(yTest.shape)


# Machine Learning basics:


# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=3,random_state=1)
# Always make sure that training data is passed not testing data
model.fit(xTrain,yTrain)

# Use x testing data to test model
predictions = model.predict(xTest)

from sklearn import metrics
accuracy = metrics.accuracy_score(predictions, yTest)

print(f"Accuracy: {accuracy}\nPercent: {accuracy * 100}%")

