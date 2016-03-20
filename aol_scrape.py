import requests
from bs4 import BeautifulSoup as bs
import pymongo
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
def aol(query,page):
	stop_words = set(stopwords.words('english'))
	stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
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
				dic["title_probablity"]=float(str(title).lower().split().count(query))/float(len(str(title).split()))
				p=soup.find("p",{"property":"f:desc"})
				desc=p.text
				list_of_words = [i.lower() for i in wordpunct_tokenize(desc) if i.lower() not in stop_words]
				dic["snippet_probablity"]=float(list_of_words.count(query))/float(len(list_of_words))
				dic["snippet"]=" ".join(list_of_words)
				source=requests.get(link).text
				soup=bs(source,"lxml")
				dic["source"]=soup.text
				db.search_results.insert(dic)
			except:
				pass

