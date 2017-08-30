# -*- coding: utf-8
from __future__ import print_function  # Only needed for Python 2

import sys
from textblob import TextBlob
f=file("city.php","w")

reload(sys)
sys.setdefaultencoding('utf-8')
header="""<?php

$data = array (
	"sessionId" => "10001.SES.18.08.2017.17.35.13.2",
	"txId" => "0",
	"deviceUUId" => "395e0e1d2f76c8f1",
	"type" => 85,
	"subType" => 0,
	"action" => 1, 
	"OID" => "",
	"fromTime" => "",
	"toTime" => "",
	"index" => 0,
	"idList" => array(),
	"info" =>array(
"""
print (header,file=f)
import string

from bs4 import BeautifulSoup
import urllib2

def php(a):
	blob = TextBlob(a)
	h="***"
	try:
		h=blob.translate(to="hi")
	except Exception, e:
		pass		
	print ("""array(
		"objectId"=> "",
		"tehsilName" => "%s",
		"districtId" => "",
		"tehsilNameHindi" => "%s",
		"creationTime" => 0,
		"modificationTime" => 0),
		"tehsilId" => ""
		,"""%(a,h),file=f)
	print ("\n\n",file=f)

url="https://en.wikipedia.org/wiki/Category:Villages_in_Uttar_Pradesh"
page = urllib2.urlopen(url)
soup=BeautifulSoup(page,'html.parser')
i=0
for text in soup.findAll("div",{"class":"mw-category"}):
	for t in text.findAll("a"):

		te=t.text.split(' ')
		te=te[2]
		php(te)
		#te= unicode(te, "utf-8")
		#print te
		#te.replace("—","-")
		
print ("))",file=file)