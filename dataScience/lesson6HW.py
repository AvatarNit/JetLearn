import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("C:/Users/sajja/OneDrive/Desktop/VSCode/dataScience/lesson6-matplotlib2/titanic.csv")

data.to_csv("titanic.csv")

# Bar graph Total Men vs. Women
males = data[data["Sex"] == "male"]
females = data[data["Sex"] == "female"]

plt.bar(["Male","Female"],[len(males),len(females)])
plt.ylabel("Number of Passengers")
plt.show()

# Bar graph Men vs Women Fare
maleFare = data.loc[data["Sex"] == "male","Fare"]
femaleFare = data.loc[data["Sex"] == "female","Fare"]
plt.bar(["Male","Female"],[maleFare.mean(),femaleFare.mean()])
plt.ylabel("Fare")
plt.title("Avg Fare")
plt.show()

# Pie chart for different classes
one = len(data[data["Pclass"] == 1])
two = len(data[data["Pclass"] == 2])
three = len(data[data["Pclass"] == 3])

classes = ["1","2","3"]
count = [one,two,three]
clr = ["g","b","r"]

plt.pie(count,labels=classes,colors=clr,startangle=90,shadow=True)
plt.title("Class Chart")
plt.show()