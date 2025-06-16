import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson1\lesson1.csv")

data.columns = ["X","Y"]

Xdata = data["X"].to_list()
Ydata = data["Y"].to_list()

print(Xdata)
print(Ydata)

tempX = []
for i in Xdata:
    tempX.append([i])

tempY = []
for i in Ydata:
    tempY.append([i])

Reg = LinearRegression()

Reg = Reg.fit(tempX,tempY)

print(f"m = {Reg.coef_[0][0]}\nc = {Reg.intercept_[0]}")