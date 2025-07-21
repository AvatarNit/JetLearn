import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson10-contentReccomendation\books.csv")

data = data[["title","description"]]

print(data.head())
print(data.info())
print(data.shape)

data["description"] = data["description"].fillna("")

print(data.info())

vectorizer = TfidfVectorizer(stop_words="english")
tdfMatrix = vectorizer.fit_transform(data["description"])

cosSim = cosine_similarity(tdfMatrix,tdfMatrix)
indices = pd.Series(data.index,index=data["title"]).drop_duplicates()

def getReccomendations(title,cosine_sim=cosSim):
  if title not in indices:
    return "Book not in dataset"
  
  idx = indices[title]
  sim_scores = list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1],reverse=True)
  sim_scores = sim_scores[1:11]
  book_indices = [i[0] for i in sim_scores]
  return data["title"].iloc[book_indices]

print("Similar Books to 'Gilead':")
print(getReccomendations("Gilead"))

print("")
print("")

print("Similar Books to 'Go Tell it on the Mountain':")
print(getReccomendations("Go Tell it on the Mountain"))