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
from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier
textTrainer = Trainer(tokenizer)
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
for t in train:
	textTrainer.train(t[0], t[1])

# When you have sufficient trained data, you are almost done and can start to use
# a classifier.
textClassifier = Classifier(textTrainer.data, tokenizer)

#cl = NaiveBayesClassifier(train)

while 0<1:
	start = time.time()

	a=raw_input("enter\n")
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
	ans=textClassifier.classify(fword)
	print(ans)
	
	print(time .time()-start)

	fb=raw_input("corect or not y/correct value \n")
	if(fb=="y"):
		textTrainer.train(fword, ans)
	    #train.append([inp,ans])
	else:
		textTrainer.train(fword, fb)
	    
	print(a)

	print("\n")

