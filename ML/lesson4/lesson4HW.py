import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson4\cat_breeds_clean.csv")

print(data.head())
print(data.info())

X = data[["Age_in_months","Gender","Body_length","Weight","Fur_colour_dominant","Fur_pattern","Eye_colour","Allowed_outdoor","Preferred_food","Owner_play_time_minutes","Sleep_time_hours"]]
y = data["Breed"]

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

X["Gender"] = encoder.fit_transform(X["Gender"])
X["Fur_colour_dominant"] = encoder.fit_transform(X["Fur_colour_dominant"])
X["Fur_pattern"] = encoder.fit_transform(X["Fur_pattern"])
X["Eye_colour"] = encoder.fit_transform(X["Eye_colour"])
X["Preferred_food"] = encoder.fit_transform(X["Preferred_food"])
y = encoder.fit_transform(y)

print(X)
print(y)

from sklearn.model_selection import train_test_split
XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=5)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()

classifier.fit(XTrain,yTrain)
yPredict = classifier.predict(XTest)


from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

sns.heatmap(confusion_matrix(yTest,yPredict),annot=True,fmt="d")

plt.title(f"Confusion Matrix (Accuracy: {round(accuracy_score(yTest,yPredict)*100,2)}%)")
plt.xlabel("Predict")
plt.ylabel("Actual")

plt.show()


print("Classification Report:\n" , classification_report(yTest,yPredict))