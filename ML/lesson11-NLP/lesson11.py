import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson11-NLP\train.txt", sep=";", names=["text","label"],nrows=5000)

print(data.head())

print(set(data["label"]))
data["label"] = data["label"].replace({'joy':0, 'sadness':1, 'love':0, 'anger':1, 'fear':1, 'surprise':0})

X = data["text"]
y = data["label"]

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
import re # Regular Expression

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
    
# Vectorizer
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(ngram_range=(1,2))
XTrainNew = cv.fit_transform(XTrainCorpus)
XTestNew = cv.transform(XTestCorpus)

print(XTestNew.shape , XTrainNew.shape)

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(XTrainNew,yTrain)

XTrainPredict = rfc.predict(XTrainNew)
XTestPredict = rfc.predict(XTestNew)

# Sentiment Analysis

# Function for new predictions

def sentimentPredict(text):
    text = transform(text)
    text = cv.transform(text)
    textPredict = rfc.predict(text)

    if textPredict[0] == 1:
        return "Negative"
    else:
        return "Positive"


str1 = ["School is coming I am sad and unhappy"]
str2 = ["First week of school is only 3 days I am happy, excited, relieved"]

print(f"Sentiment Prediction:\n   Str1: {sentimentPredict(str1)}\n   Str2: {sentimentPredict(str2)}")
