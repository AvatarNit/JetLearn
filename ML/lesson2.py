import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson2\titanic.csv")

X = data[["Age","Sex","Pclass"]]
y = data["Survived"]

X["Sex"] = X["Sex"].map({"male":0,"female":1})

print(X.info())
print(y.info())

from sklearn.model_selection import train_test_split

XTrain,XTest,YTrain,YTest = train_test_split(X,y,test_size=0.2,random_state=5)

print(XTrain.shape)
# Multi variable regression

from sklearn.linear_model import LinearRegression

Reg = LinearRegression()

Reg.fit(XTrain,YTrain)

from sklearn.metrics import mean_squared_error

YTestPredict = Reg.predict(XTest)

rmse = np.sqrt(mean_squared_error(YTest,YTestPredict))
print("RMSE Multi-Var: " , rmse)

# Polynomial Regression

from sklearn.preprocessing import PolynomialFeatures

polyFeat = PolynomialFeatures(degree=2)

XTrainPoly = polyFeat.fit_transform(XTrain)
XTestPoly = polyFeat.fit_transform(XTest)

polyReg = LinearRegression()
polyReg.fit(XTrainPoly,YTrain)

YTestPredictPoly = polyReg.predict(XTestPoly)

rmsePoly = np.sqrt(mean_squared_error(YTest,YTestPredictPoly))
print("RMSE Poly: " , rmsePoly)
