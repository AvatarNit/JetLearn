import pandas as pd

data = pd.read_csv("C:/Users/sajja/OneDrive/Desktop/VSCode/dataScience/lesson4-pandas2/titanic.csv")

print(data.groupby(["Sex","Pclass"])["Age"].mean())
print("Median age of survived:" , data[data["Survived"] == 1]["Age"].mean())