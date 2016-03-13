from bs4 import BeautifulSoup as bs
import requests
import pymongo
def ask(query,pages):
	client=pymongo.MongoClient()
	db=client.text_mining
	for j in range(1,int(pages)+1):
		data=requests.get("http://www.ask.com/web?q="+query+"&page="+str(j)).text
		data=data.split('<h2 class="web-result-title">')
		data=data[1:]
		for i in data:
			dic={}
			dic["search_engine"]="ask"
			dic["query"]=query
			soup=bs(i,"lxml")
			a=soup.find("a")
			dic["link"]=a.get("href")
			p=soup.find("p",{"class":"web-result-description"})
			dic["snippet"]=p.text
			source=requests.get(dic["link"]).text
			soup=bs(source,"lxml")
			dic["source"]=soup.text
			db.search_results.insert(dic)
	
