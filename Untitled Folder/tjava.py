# -*- coding: utf-8 -*-

from textblob import Word
import string
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from stemming.porter2 import stem
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import time

nltk.download('stopwords')
train = [
    ('water', 'water'),
    ('log', 'water'),
    ('jal', 'water'),
    ('drain', 'water'),
    ('sewag', 'water'),
    ('burgler', 'police'),
    ('thief', 'police'),
    ('robbery', 'police'),
    ('murder', 'police'),
    ('medicin', 'doctor'),
    ('ill', 'doctor'),
    ('sick', 'doctor'),
    ('accident', 'doctor'),

    

]
cl = NaiveBayesClassifier(train)

	
start = time.time()
f=file("inp","r")
a=f.readLine()
f.close()
a=a.lower()
replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
a = a.translate(replace_punctuation)
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(a)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
			b=Word(w)
			#t=t.replace(w,b.lemmatize())
			# use porterstemming for faster
			filtered_sentence.append(stem(b))



fword=' '.join(filtered_sentence)
print("lamentized sentence by porter ="+fword)	
ans=cl.classify(fword)
print(ans)
print(cl)
print(time .time()-start)
f=file("inp2","r")
a=f.readLine()
f.close()

fb=raw_input("corect or not y/correct value \n")
if(fb=="y"):
	fe=[(fword,ans)]
	cl.update(fe)
    #train.append([inp,ans])
else:
	fe=[(fword,fb)]
	cl.update(fe)
print(a)

print("\n")

