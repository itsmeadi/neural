import pymongo
import pprint
from pymongo import MongoClient
c=MongoClient('localhost',27017)
db=c['CrispyClips']
collection=db['LanguageMaster']
for doc in collection.find():
	pprint.pprint(doc)
	pass