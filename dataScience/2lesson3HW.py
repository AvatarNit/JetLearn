import pandas as pd

data = pd.read_csv("C:/Users/sajja/OneDrive/Desktop/VSCode/dataScience/lesson3-pandas/iris.csv")

print(data.head())
print(data.shape)
print(data.info())
print(data.describe())
print(data[["sepal_length"]].max())
print(data["species"].value_counts())
