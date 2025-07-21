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

# Text Transfomation
wne = WordNetLemmatizer()

def transform(data):
    corpus = []
    




# Sentiment Analysis
