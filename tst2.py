from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [
('2','4'),
('4','8'),('6','12'),('8','16'),('10','20')
]
while 0<1:

    cl = NaiveBayesClassifier(train)
    inp=raw_input("enter a sentence     \n")
    ans=cl.classify(inp)
    print(ans)
    fb=raw_input("corect or not y/n \n")
    if(fb=="y"):
        train.append([inp,ans])
    elif(ans=='pos'):
        train.append([inp,'neg'])
    elif(ans=='neg'):
        train.append([inp,'pos'])

        
    




from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [
('2','4'),
('4','8'),('6','12'),('8','16'),('10','20')
]


cl = NaiveBayesClassifier(train)

# Classify some text
inp=raw_input("enter a sentence     \n")
print(cl.classify(inp))


# Show 5 most informative features
cl.show_informative_features(5)