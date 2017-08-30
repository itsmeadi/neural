from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

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

while 0<1:
    print(cl.show_informative_features(5))
    inp=raw_input("enter a sentence     \n")
    ans=cl.classify(inp)
    print(ans)
    fb=raw_input("corect or not y/n \n")
    if(fb=="y"):
        fe=[(inp,ans)]
        cl.update(fe)
        #train.append([inp,ans])