
header="""<?php

$data = array (
	"sessionId" => "10001.SES.18.08.2017.17.35.13.2",
	"txId" => "0",
	"deviceUUId" => "395e0e1d2f76c8f1",
	"type" => 84,
	"subType" => 0,
	"action" => 1, 
	"OID" => "",
	"fromTime" => "",
	"toTime" => "",
	"index" => 0,
	"idList" => array(),
	"info" =>array(
"""
def pri(n,h,p):
	print """	array(
		"objectId"=> "",
		"blockName" => "%s",
		"cityId" => "%s",
		"blockNameHindi" => "%s",
		"creationTime" => 0,
		"modificationTime" => 0),
"""%(n,p,h)
	pass

p=""

fe=file("v.txt","r")
fh=file("vh.txt","r")
le=fe.readlines()
lh=fh.readlines()
print "le=",le
i=0
for l1 in le:
	print i
	e=l1.split("=")
	h=lh[i].split("=")
	if(e[0].contains("Tehsil")):
		p=l[0]
	elif(e[0].contains("Block")):
		pri(l[0],h,t)
	i=i+1
	pass