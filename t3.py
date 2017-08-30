
# -*- coding: utf-8 -b*-


#This code is for training and testing puspose only
#-Aditya Agarwal
print "This code is for training and testing puspose only"

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

#nltk.download('stopwords')			#THIS line needed to be execeuted once on a system	


def detect_language(line):
	line = unicode(line, "utf-8")
	maxchar = max(line)
	if u'\u0900' <= maxchar <= u'\u097f':
	    return 'hindi'
	return 'english'
train = [			#default training set
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
def load_Train():		#Load traing set from train.pickle file
	f=None
	global linecount
	global cl
	try:
		f = open('train.pickle', 'rb')
		cl = pickle.load(f)
		f.close()
		fl=open("nol","r")
		linecount=int(fl.read())
		print "Reading complaints from complaints file"
		fl.close()
		f.close()
	
	except Exception, e:
		cl = NaiveBayesClassifier(train)	#Train from default training set in case of file not found
		linecount=0
		print e
	#print("No of lines="+str(linecount))
	return cl
	
def signal_handler(signal, frame):		#ctrl c to dump data
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
	print("Stemmed sentence by porter ="+a)
	return a
def categorize(a):
	if(detect_language(a)=='english'):	#since Hindi sentences cannot be stemmed
		a=stemm(a)			
	ans=cl.classify(a)
	return ans
	pass
#fw='दवा'	
linecount=0
cl=load_Train()
#print("linecount1="+str(linecount))

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
#print train

ff=file("trainn")
lc=0
if(linecount!=0):
	lc=linecount
	linecount=0
#print("linecount2="+str(lc))
print "Press Ctrl-C to dump training data and exit"
print "Press Ctrl-Z to exit without dump"
print "Enter new keyword to input new complaint outside training set"
print "\n"
for line in ff:
	linecount+=1
	if(linecount<lc):
		continue

	line=line.strip()
	print "Complaint=",line
	start = time.time()

	#a=raw_input("enter\n")
	a=line
	#a='दवा'
	ans=categorize(a)
	print "category calculated=",ans
	#print(cl)
	#print(time.time()-start)

	fb=raw_input("correct or not y/correct value/new \n")
	if(fb=="y"):
		print ("yes")
		fe=[(a,ans)]
		cl.update(fe)
	    #train.append([inp,ans])
	elif(fb=="new"):
		a=raw_input("Enter a sentence\n")
		if(detect_language(a)=='english'):
			a=stemm(a)
		print(cl.classify(a))
	
	elif(fb!="n" and fb!=''):
		print ("no")
		fe=[(a,fb)]
		cl.update(fe)
		
	
	# print(a)
	
	print("\n")


