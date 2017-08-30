# -*- coding: utf-8 -*-

from itertools import chain
from nltk.corpus import indian
from nltk.util import ngrams
from nltk import NaiveBayesClassifier as nbc


# NLTK reads the corpus as bytecodes.
hindi = " ".join(indian.words('hindi.pos'))
bangla = " ".join(indian.words('bangla.pos'))
marathi = " ".join(indian.words('marathi.pos'))
telugu = " ".join(indian.words('telugu.pos'))

# Prints out first 10 bytes (including spaces).
print 'hindi:', hindi[:10]
print 'bangla:', bangla[:10]
print 'marathi:', marathi[:10]
print 'telugu:', telugu[:10]
print
# Allocate some sort of labels for the data.
training = [(hindi, 'hi'), (bangla, 'ba'), (marathi, 'ma'), (telugu, 'te')]
print training	

# This is how you can extract ngrams
print ngrams(telugu[:10], 2)
print
print (hindi[:10], 3)

print

print

print

vocabulary = set(chain(*[ngrams(txt, 2) for txt,tag in training]))
feature_set = [({i:(i in ngrams(sentence, 2)) for i in vocabulary},tag) for sentence, tag in training]

classifer = nbc.train(feature_set)

test1 = u'पूर्ण प्रत' # hindi
test2 = u'মহিষের সন্' # bangla
test3 = u'सनातनवा' # marathi
test4 = u'ఆడిట్ ' # telugu

for testdoc in [test1, test2, test3, test4]:
    featurized_test_sent =  {i:(i in ngrams(testdoc,2)) for i in vocabulary}
    print "test sent:", testdoc
    print "tag:", classifer.classify(featurized_test_sent)
    print



