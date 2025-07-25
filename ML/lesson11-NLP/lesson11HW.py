import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson11-NLP\emotion_sentimen_dataset.csv",nrows=5000)

print(data.head())

print(set(data["Emotion"]))
data["Emotion"] = data["Emotion"].replace({'love':1, 'relief':1, 'empty':-1, 'enthusiasm':1, 'worry':-1, 'sadness':-1, 'hate':-1, 'happiness':1, 'surprise':1, 'neutral':0, 'fun':1, 'anger':-1})

X = data["text"]
y = data["Emotion"]

XTrain,XTest,yTrain,yTest = train_test_split(X,y,test_size=0.2,random_state=2)

import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("stopwords")
nltk.download("wordnet")

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# Text Transformation
wne = WordNetLemmatizer()

def transform(data):
    corpus = []

    for i in data:
        newi = re.sub("[^a-zA-Z]", " ", i)
        newi = newi.lower()
        newi = newi.split()
        tempList = [wne.lemmatize(word) for word in newi if word not in stopwords.words("english")]
        corpus.append(" ".join(tempList))
    return corpus

XTrainCorpus = transform(XTrain)
XTestCorpus = transform(XTest)

print(XTrainCorpus[0:5])

# Vectorize
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(ngram_range=(1,2))

XTrainNew = cv.fit_transform(XTrainCorpus)
XTestNew = cv.transform(XTestCorpus)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100)

rfc.fit(XTrainNew,yTrain)

XTrainPredict = rfc.predict(XTrainNew)
XTestPredict = rfc.predict(XTestNew)

def sentimentPredict(text):
    text = transform(text)
    text = cv.transform(text)
    textPredict = rfc.predict(text)

    if textPredict[0] == 1:
        return "Positive"
    elif textPredict[0] == 0:
        return "Neutral"
    else:
        return "Negative"

str1 = ["School is coming I am sad and unhappy"]
str2 = ["First week of school is only 3 days I am happy, excited, relieved"]
str3 = ["School is work"]

print(f"Sentiment Predict:\n   Str1: {sentimentPredict(str1)}\n   Str2: {sentimentPredict(str2)}\n   Str3: {sentimentPredict(str3)}")