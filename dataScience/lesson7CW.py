import numpy as np
import pandas as pd

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\dataScience\lesson7-DataPreProcessing\Data.csv")

print(data.info())
print(data.head())

X = data.iloc[:,:-1].values #picked all execept last(-1)
y = data.iloc[:,-1].values #picked last(-1)

print("Features:\n" , X)
print("Target:\n" , y)


# Replace Null Values:

from sklearn.impute import SimpleImputer
# Intitalize function
imputer = SimpleImputer(missing_values=np.nan, strategy="mean") # replace missing values with the mean of the column

X[:,1:3] = imputer.fit_transform(X[:,1:3])
print("After Imputing: \n" , X)

# Convert columns to numerical

#  Just 1 & 0 encoding:
from sklearn.preprocessing import LabelEncoder
# intitalize
encoder = LabelEncoder()
y = encoder.fit_transform(y)
print("After encoding: \n" , y) # [0 1 0 0 1 1 0 1 0 1]

# Multi number encoding:
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [0])], remainder="passthrough")
X = pd.DataFrame(ct.fit_transform(X))

print("After encoding: \n" , X)

# Splitting data
from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(X,y, test_size=0.2, random_state=1) # Test_size is percent
print(f"xTrain:\n {xTrain}\nxTest:\n {xTest}\nyTrain: {yTrain}\nyTest: {yTest}")

# Scaling down to -1 -> 1
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

xTrain.iloc[:,1:3] = scaler.fit_transform(xTrain.iloc[:,1:3])
xTest.iloc[:,1:3] = scaler.fit_transform(xTest.iloc[:,1:3])
print(f"After scaling:\n   xTrain:\n {xTrain}\n   xTest:\n {xTest}")
