import json
import pymongo
import urllib.request
import os
from bs4 import BeautifulSoup as bs
def parse(fname):
	client=pymongo.MongoClient()
	db=client.text_mining
	db.search_results.remove({})
	f=open(fname,"r").read()
	g=json.loads(f)
	for i in g:
		dic={}
		dic["search_engine"]=i["search_engine_name"]
		dic["query"]=i["query"]
		for j in i["results"]:
			dic["domain"]=j["domain"]
			dic["link"]=j["link"]
			try:
				with urllib.request.urlopen(j["link"]) as response:
					html = response.read()
				soup=bs(html,"lxml")
				dic["source"]=soup.text
			except:
				pass
			dic["snippet"]=j["snippet"]
			dic["title"]=j["title"]
			db.search_results.insert(dic)
			del dic["_id"]
	os.remove(fname)
