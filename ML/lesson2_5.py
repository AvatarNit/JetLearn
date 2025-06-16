import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson2\iris.csv")

X = data[["sepal_length","sepal_width","petal_length","petal_width"]]
y = data["species"].map({'versicolor':0, 'setosa':1, 'virginica':2})

print(data.info())
print(set(y))
print(X.info())
print(y.info())

from sklearn.model_selection import train_test_split

XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=5)


# Multi Var
from sklearn.linear_model import LinearRegression
Reg = LinearRegression()

Reg.fit(XTrain,yTrain)

yTestPredict = Reg.predict(XTest)

from sklearn.metrics import mean_squared_error

rmse = np.sqrt(mean_squared_error(yTest,yTestPredict))
print("RMSE Multi-Var: " , rmse)

# Poly

from sklearn.preprocessing import PolynomialFeatures

polyFeat = PolynomialFeatures(degree=4)

XTrainPoly = polyFeat.fit_transform(XTrain)
XTestPoly = polyFeat.fit_transform(XTest)

polyReg = LinearRegression()
polyReg.fit(XTrainPoly,yTrain)

yTestPredictPoly = polyReg.predict(XTestPoly)

rmsePoly = np.sqrt(mean_squared_error(yTest,yTestPredictPoly))
print("RMSE Poly: " , rmsePoly)