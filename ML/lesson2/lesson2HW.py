import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson2\forestfires.csv")

X = data[["month","day","FFMC","DMC","DC","ISI","temp","RH","wind","rain"]]
y = data["area"]

X["month"] = X["month"].map({"jan":0,"feb":1,"mar":2,"apr":3,"may":4,"jun":5,"jul":6,"aug":7,"sep":8,"oct":9,"nov":10,"dec":11})
X["day"] = X["day"].map({"mon":0,"tue":1,"wed":2,"thu":3,"fri":4,"sat":5,"sun":6})

print(data.info())
print(X.info())
print(y.info())

from sklearn.model_selection import train_test_split

XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=5)


# Multi Var
from sklearn.linear_model import LinearRegression
Reg = LinearRegression()

Reg.fit(XTrain,yTrain)

yTestPredict = Reg.predict(XTest)

from sklearn.metrics import accuracy_score

# print("Accuracy Multi-Var: " , accuracy_score(yTest,yTestPredict))

from sklearn.metrics import mean_squared_error

rmse = np.sqrt(mean_squared_error(yTest,yTestPredict))
print("RMSE Multi-Var: " , rmse)

# Poly

from sklearn.preprocessing import PolynomialFeatures

polyFeat = PolynomialFeatures(degree=10)

XTrainPoly = polyFeat.fit_transform(XTrain)
XTestPoly = polyFeat.fit_transform(XTest)

polyReg = LinearRegression()
polyReg.fit(XTrainPoly,yTrain)

yTestPredictPoly = polyReg.predict(XTestPoly)

# print("Accuracy Poly: " , accuracy_score(yTest,yTestPredictPoly))

rmsePoly = np.sqrt(mean_squared_error(yTest,yTestPredictPoly))
print("RMSE Poly: " , rmsePoly)