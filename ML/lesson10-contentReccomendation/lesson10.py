import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson10-contentReccomendation\movies_metadata.csv",nrows=5000)

print(data.head())

data["overview"] = data["overview"].fillna("")

vectorizer = TfidfVectorizer(stop_words="english")
tdfMatrix = vectorizer.fit_transform(data["overview"])

# Find cosine similarity
cosSim = cosine_similarity(tdfMatrix,tdfMatrix)
indices = pd.Series(data.index,index=data["title"]).drop_duplicates()

def getReccomendations(title,cosine_sim=cosSim):
  if title not in indices:
    return "Movie not in dataset"
  
  idx = indices[title]
  sim_scores = list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1],reverse=True)
  sim_scores = sim_scores[1:11]
  movie_indices = [i[0] for i in sim_scores]
  return data["title"].iloc[movie_indices]

print("Similar Movies:")
print(getReccomendations("Toy Story 2"))