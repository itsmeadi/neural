# -*- coding: utf-8
from textblob import Word
import string
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from stemming.porter2 import stem
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import time

#nltk.download('stopwords')
def detect_language(line):
	line = unicode(line, "utf-8")
	
	maxchar = max(line)
	if u'\u0900' <= maxchar <= u'\u097f':
	    return 'hindi'
	return 'english'
train = [
    ('water', 'water'),
    ('log', 'water'),
    ('jal', 'water'),
    ('drainag', 'water'),
    ('sewag', 'water'),
    ('burgler', 'police'),
    ('thief', 'police'),
    ('robbery', 'police'),
    ('murder', 'police'),
    ('medicin', 'doctor'),
    ('ill', 'doctor'),
    ('sick', 'doctor'),
    ('accident', 'doctor'),
    ('dog', 'municipal'),
    ('waste', 'municipal'),
    ('garbage', 'municipal'),
    ('illegal', 'police'),
    ('animal', 'municipal'),
    ('light', 'electrical'),
    (u'दवा', 'doctor'),
    (u'बीमार', 'doctor'),

]
cl = NaiveBayesClassifier(train)

while 0<1:
	start = time.time()

	a=raw_input("Input.......\n")
	#a='दवा'
	at=a
	if(detect_language(a)=='english'):
		a=a.lower()
		#print ord(a[0])
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
		
		a=' '.join(filtered_sentence)
		print("lamentized sentence by porter ="+a)
		#fw='दवा'	

	ans=cl.classify(a)
	print(ans)
	print(cl)
	#print(time.time()-start)
	if(detect_language(at)=='hindi'):
		a = unicode(a, "utf-8")
	
	fb=raw_input("correct or not y/correct value \n")
	if(fb=="y"):
		fe=[(a,ans)]
		cl.update(fe)
	    #train.append([inp,ans])
	elif(fb!="n"):
		fe=[(a,fb)]
		cl.update(fe)
	# print(a)

	print("\n")

