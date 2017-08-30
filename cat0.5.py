# -*- coding: utf-8 -*-

import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB



from textblob import Word
import string
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from stemming.porter2 import stem
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import time
train = [
    ('water', 'water'),
    ('water', 'water'),
    ('water', 'water'),
    ('log', 'water'),
    ('jal', 'water'),
    ('drain', 'water'),
    ('sewag', 'water'),
    ('burgler', 'police'),
    ('मौत', 'police'),
    ('thief', 'police'),
    ('robbery', 'police'),
    ('murder', 'police'),
    ('medicin', 'doctor'),
    ('ill', 'doctor'),
    ('sick', 'doctor'),
    ('दवा', 'doctor'),
    ('बीमार', 'doctor'),

]
def dataFrame():
    rows = []
    index = []
    for message, cat in train:
        rows.append({'message': message, 'class': cat})
        #index.append(filename)

    return DataFrame(rows)

data = DataFrame({'message': [], 'class': []})

data = data.append(dataFrame())


vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)
print counts
classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)


#examples = ['water logging','murders']
e=raw_input("Enter\n")   

e=e.lower()
replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
e = e.translate(replace_punctuation)
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(e)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
            b=Word(w)
            #t=t.replace(w,b.lemmatize())
            # use porterstemming for faster
            filtered_sentence.append(stem(b))



e=' '.join(filtered_sentence)
print("lemantized sentence="+e)
e=[e]

example_counts = vectorizer.transform(e)
print("\n")
print example_counts
predictions = classifier.predict(example_counts)
print predictions[0]


