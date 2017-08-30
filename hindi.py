# -*- coding: utf-8 -*-

from textblob import Word
import string
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob



train = [
    
('हिन्दी','हिन्दी')
    

]
cl = NaiveBayesClassifier(train)
ans=cl.classify("हिन्दी")
print(ans)
