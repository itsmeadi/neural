# -*- coding: utf-8 -*-
from textblob import TextBlob
from textblob import Word
a=raw_input(u"enter any lang\n")
#b=TextBlob(u'जल भराव')
b=TextBlob(a)
print('spell check=')
print(b.correct)
#b=TextBlob(b.correct)

print('\n')
print('input language='+b.detect_language())
print('translated to')
try:
	print(b.translate(to='hi'))
except:
	pass
print('\n')
print(b.lemmatize())

