# -*- coding: utf-8

import string

from bs4 import BeautifulSoup
import urllib2
for x in xrange(21,100):
	url="https://www.consumercomplaints.in/bysubcategory/municipal-corporation/page/"+str(x)
	page = urllib2.urlopen(url)
	soup=BeautifulSoup(page,'html.parser')
	for text in soup.findAll("td",{"class":"complaint"}):
		for t in text.findAll("a"):

			te=t.text
			#te= unicode(te, "utf-8")
			#print te
			#te.replace("—","-")
			t1=te.split(u" — ")
			print t1[1]
		
		
