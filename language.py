# -*- coding: utf-8 -*-
from textblob import TextBlob
a=raw_input(u"enter any lang\n")
print a
print(ord(u'ट'))
for ab in a:
	print(ab)

#a=u"ट"
b=TextBlob(a)
print(b.detect_language())
try:
	print(b.translate(to="hi"))
except:
	try:
		print(b.translate(to="en"))
	except:
		print ""


