import requests
from bs4 import BeautifulSoup as bs
import pymongo
def aol(query,page):
	client=pymongo.MongoClient()
	db=client.text_mining
	for k in range(1,int(page)+1):
		data=requests.get("http://search.aol.com/aol/search?s_it=topsearchbox.search&v_t=na&q="+query+"&page="+str(k))
		f=data.text
		f=f.split('<h3 class="hac">')
		f=f[1:]
		for i in f:
			try:
				soup=bs(i,"lxml")
				a=soup.find("a",{"rel":"f:url"})
				link=a.get("href")
				dic={}
				dic["query"]=query
				dic["search_engine"]="aol"
				dic["link"]=link
				title=a.text
				dic["title"]=title
				p=soup.find("p",{"property":"f:desc"})
				desc=p.text
				dic["snippet"]=desc
				dic["source"]=requests.get(link).text
				db.search_results.insert(dic)
			except:
				pass

