# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sel1="चुनें"
sel="Select"

f=file("v.txt","r")
for line in f.readlines():
	if(sel not in line):
		print line.strip()

	pass