# -*- coding: utf-8 -b*-
from textblob import Word
import string
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from stemming.porter2 import stem
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import time
import pickle
import signal
import sys

#nltk.download('stopwords')		#THIS line needed to be execeuted once on a system	
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
#cl=NaiveBayesClassifier(tr)
#cl = NaiveBayesClassifier(train)
def load_Train():
	f=None
	global linecount
	global cl
	try:
		f = open('train.pickle', 'rb')
		cl = pickle.load(f)
		f.close()
		fl=open("nol","r")
		linecount=int(fl.read())
		fl.close()
		f.close()
	
	except Exception, e:
		cl = NaiveBayesClassifier(train)
		linecount=0

	print("No of lines="+str(linecount))
	return cl
	
def signal_handler(signal, frame):
	f=open("train.pickle","wb")
	fl=open("nol","wb")
	fl.write(str(linecount))
	fl.close()
	print("Dumping data.....")
	pickle.dump(cl,f);
	f.close()
	print("Dumping Complete")
	sys.exit(0)
	
signal.signal(signal.SIGINT, signal_handler)

def stemm(a):
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
	return a
def categorize(a):
	if(detect_language(a)=='english'):
		a=stemm(a)
	ans=cl.classify(a)
	return ans
	pass
#fw='दवा'	
linecount=0
cl=load_Train()
print("linecount1="+str(linecount))

i=0
print cl
stop_words = set(stopwords.words('english'))

for w,l in train:
		    if w not in stop_words:
				b=Word(w)
				#t=t.replace(w,b.lemmatize())
				# use porterstemming for faster
				train[i]=(stem(b),l)
				i=i+1
print train

ff=file("train")
lc=0
if(linecount!=0):
	lc=linecount
	linecount=0
print("linecount2="+str(lc))
while (0<1):
	a=raw_input("enter\n")
	#a=line
	#a='दवा'
	ans=categorize(a)
	print(ans)
	print(cl)

	fb=raw_input("correct or not y/correct value \n")
	if(fb=="y"):
		print ("yes")
		fe=[(a,ans)]
		cl.update(fe)
	    #train.append([inp,ans])
	elif(fb=="new"):
		a=raw_input("Enter a sentence\n")
		print(cl.classify(a))

	elif(fb!="n" and fb!=''):
		print ("no")
		fe=[(a,fb)]
		cl.update(fe)
		

	# print(a)

	print("\n")


