import pandas as pd

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson9-simpleReccomendation\restaurants.csv")

print(data.head())
print(data.info())
print(data.shape)

data = data[["Restaurant Name","Aggregate rating","Votes"]]

print(data.head())
print(data.info())
print(data.shape)

"""
Weighted Rating: (v/v+m)*R + (m/v+m)*C

v - num votes(vote_count)
m - min votes to qualify
R - Avg rating for movie (vote_average)
C - Mean votes
"""

m = data["Votes"].quantile(0.9)
C = data["Aggregate rating"].mean()
print(f"m: {m}\nC: {C}")

qualifiedRest = data.copy().loc[data["Votes"] >= m]

print("Num qualified rests: " , qualifiedRest.shape)

def weightedRating(x):
    v = x["Votes"]
    R = x["Aggregate rating"]

    return ((v/(v+m))*R) + ((m/(v+m))*C)

# Creating new column score and calling the weightedRating() for each row
qualifiedRest["score"] = qualifiedRest.apply(weightedRating,axis=1)

qualifiedRest = qualifiedRest.sort_values("score",ascending=False)

print("Top 20 Restraunts:\n" , qualifiedRest[["Restaurant Name","Aggregate rating","Votes","score"]].head(20))

qualifiedRest = qualifiedRest.sort_values("score")
print("Bottom 20 Restraunts:\n" , qualifiedRest[["Restaurant Name","Aggregate rating","Votes","score"]].head(20))