import pandas as pd

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\dataScience\lesson8-ML\titanic.csv")

# Check if null values present:
print(data.head())
print(data.info())
    # No Null values

# Replace "Male":1, "Female":0
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

print("Before encoding: \n" , data["Sex"])
data["Sex"] = encoder.fit_transform(data["Sex"])
print("After encoding: \n" , data["Sex"])

# Scale Age down between -1 -> 1
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

data["Age"] = scaler.fit_transform(data[["Age"]])
print("Data after scaling: " , data["Age"])


# Define inputs and output
X = data[["Pclass","Sex","Age"]]
y = data["Survived"]

print(X.head())
print(y.head())


# Split test and train
from sklearn.model_selection import train_test_split

xTrain, xTest, yTrain, yTest = train_test_split(X,y, test_size=0.2, random_state=1)

print(xTrain.shape)
print(xTest.shape)
print(yTrain.shape)
print(yTest.shape)

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=3,random_state=1)
model.fit(xTrain,yTrain)

predictions = model.predict(xTest)

from sklearn import metrics
accuracy = metrics.accuracy_score(predictions, yTest)

print(f"Accuracy: {accuracy}\nPercent: {accuracy * 100}%")
