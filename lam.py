from textblob import Word
import string
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from stemming.porter2 import stem
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
nltk.download('stopwords')
train = [
    ('water', 'water'),
    ('log', 'water'),
    ('jal', 'water'),
    ('drain', 'water'),
    ('sewage', 'water'),
    ('burgler', 'police'),
    ('thief', 'police'),
    ('robbery', 'police'),
    ('murder', 'police'),
    ('medicine', 'doctor'),
    ('ill', 'doctor'),
    ('sick', 'doctor'),
    ('accident', 'doctor'),
]
cl = NaiveBayesClassifier(train)

def removearticles(text):
	articles = {'a ','an ','and ','the ','there ','is ','in ','am ','are ','were ','was '}
	for i in articles:
	    text = text.replace(i,'')
	return text

#punctuation




while 0<1:
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
    	    filtered_sentence.append(w)
    	    	b=Word(w)
				#t=t.replace(w,b.lemmatize())
				# use porterstemming for faster
				filtered_sentence=filtered_sentence.replace(w,stem(b))
	
 


	print("lamentized sentence by porter ="+a)	
	ans=cl.classify(a)

	print(ans)
	fb=raw_input("corect or not y/n \n")
	if(fb=="y"):
	    fe=[(a,ans)]
	    cl.update(fe)
	    #train.append([inp,ans])
	print(a)
	print("\n")

