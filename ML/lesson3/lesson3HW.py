import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson3\Social_Network_Ads.csv")

print(data.info)
print(data.isnull().sum())

data.drop("User ID", axis= 1, inplace=True)


from sklearn.preprocessing import LabelEncoder
labelEncoder = LabelEncoder()
data["Gender"] = labelEncoder.fit_transform(data["Gender"])

print(data.head())

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data.iloc[:,2:3] = scaler.fit_transform(data.iloc[:,2:3])
print(data.head())


X = data[["Gender","Age","EstimatedSalary"]]
y = data["Purchased"]

from sklearn.model_selection import train_test_split
XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=2)

from sklearn.linear_model import LogisticRegression
Reg = LogisticRegression()
Reg.fit(XTrain,yTrain)
yTestPredict = Reg.predict(XTest)


from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(yTest,yTestPredict)
sns.heatmap(matrix,annot=True,fmt="d")

plt.title("Confusion Matrix")
plt.xlabel("Prediction")
plt.ylabel("Actual")
plt.show()


from sklearn.metrics import accuracy_score
print(f"Acurracy: {accuracy_score(yTest,yTestPredict) * 100}%")