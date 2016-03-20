import json
import pymongo
import urllib.request
import os
from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
def parse(fname):
	stop_words = set(stopwords.words('english'))
	stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
	client=pymongo.MongoClient()
	db=client.text_mining
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
			list_of_words = [i.lower() for i in wordpunct_tokenize(j["snippet"]) if i.lower() not in stop_words]
			dic["snippet"]=" ".join(list_of_words)
			dic["snippet_probablity"]=float(list_of_words.count(i["query"].lower()))/float(len(list_of_words))
			dic["title"]=j["title"]
			dic["title_probablity"]=float(j["title"].lower().split().count(i["query"].lower()))/float(len(j["title"].split()))
			db.search_results.insert(dic)
			del dic["_id"]
	os.remove(fname)
def duckduckgo(query):
	try:
		dic={}
		dic["query"]=query
		dic["search_engine"]="duckduckgo"
		query=query.replace(" ","%20")
		import requests
		r=requests.get("https://api.duckduckgo.com/?q="+query+"&format=json")
		d=r.json()
		dic["abstract"]=d["Abstract"]
		dic["link"]=d["Results"][0]["FirstURL"]
		dic["snippet"]=d["Results"][0]["Text"]
		client=pymongo.MongoClient()
		db=client.text_mining
		db.search_results.insert(dic)
	except Exception as e:
		print (e)
		pass
	
