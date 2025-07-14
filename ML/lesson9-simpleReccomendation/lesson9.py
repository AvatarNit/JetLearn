# Recomendation System
# 1. Simple, 2.Content Based, 3.Collabrative

import pandas as pd

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson9-simpleReccomendation\movies_metadata.csv")

print(data.info())
print(data.shape)
print(data.head())

"""
Weighted Rating: (v/v+m)*R + (m/v+m)*C

v - num votes(vote_count)
m - min votes to qualify
R - Avg rating for movie (vote_average)
C - Mean votes
"""

C = data["vote_average"].mean()
print("Mean vote_avg: " , C)

m = data["vote_count"].quantile(0.90)
print("m: " , m)


# Filter qualified moveis
qualifiedMovs = data.copy().loc[data["vote_count"] >= m]

print("Num qualified mov: " , qualifiedMovs.shape)

def weightedRating(x):
    v = x["vote_count"]
    R = x["vote_average"]

    return ((v/(v+m))*R) + ((m/(v+m))*C)

# Creating new column score and calling the weightedRating() for each row
qualifiedMovs["score"] = qualifiedMovs.apply(weightedRating,axis=1)

qualifiedMovs = qualifiedMovs.sort_values("score",ascending=False)

print("Top 20 Movies:\n" , qualifiedMovs[["title","vote_average","vote_count","score"]].head(20))

qualifiedMovs = qualifiedMovs.sort_values("score")

print("Bottom 20 Movies:\n" , qualifiedMovs[["title","vote_average","vote_count","score"]].head(20))

print("Middle Movie: " , qualifiedMovs.iloc[2277]["title"])