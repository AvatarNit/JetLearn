import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson6-RandomForestClassifier\cat_breeds_clean.csv")

print(data.head())
print(data.info())


from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

data["Gender"] = encoder.fit_transform(data["Gender"])
data["Fur_colour_dominant"] = encoder.fit_transform(data["Fur_colour_dominant"])
data["Fur_pattern"] = encoder.fit_transform(data["Fur_pattern"])
data["Eye_colour"] = encoder.fit_transform(data["Eye_colour"])
data["Preferred_food"] = encoder.fit_transform(data["Preferred_food"])
data["Breed"] = encoder.fit_transform(data["Breed"])

X = data[["Age_in_months","Gender","Body_length","Weight","Fur_colour_dominant","Fur_pattern","Eye_colour","Allowed_outdoor","Preferred_food","Owner_play_time_minutes","Sleep_time_hours"]]
y = data["Breed"]

print(X)
print(y)

from sklearn.model_selection import train_test_split
XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=5)

from sklearn.tree import DecisionTreeClassifier
treeClassifier = DecisionTreeClassifier()
treeClassifier.fit(XTrain,yTrain)
yPredictTree = treeClassifier.predict(XTest)

from sklearn.ensemble import RandomForestClassifier
forestClassifier = RandomForestClassifier(n_estimators=100)
forestClassifier.fit(XTrain,yTrain)
yPredictForest = forestClassifier.predict(XTest)



from sklearn.metrics import confusion_matrix,accuracy_score

sns.heatmap(confusion_matrix(yTest,yPredictTree),annot=True,fmt="d")

plt.title(f"Confusion Matrix ({round(accuracy_score(yTest,yPredictTree)*100,5)}%)")
plt.xlabel("Predict")
plt.ylabel("Actual")

plt.show()

sns.heatmap(confusion_matrix(yTest,yPredictForest),annot=True,fmt="d")

plt.title(f"Confusion Matrix ({round(accuracy_score(yTest,yPredictForest)*100,5)}%)")
plt.xlabel("Predict")
plt.ylabel("Actual")

plt.show()