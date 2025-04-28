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