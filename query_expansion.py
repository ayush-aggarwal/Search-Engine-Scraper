import pymongo
import enchant
d = enchant.Dict("en_US")
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
client=pymongo.MongoClient()
db=client.text_mining
query="github"
#for summary
res=list(db.search_results.find({"search_engine":"duckduckgo","query":query}))
if len(res)!=0:
	print "Summary of the query '"+query+"' is:- "
	print res[0]["abstract"]
	print res[0]["link"]+" ("+res[0]["snippet"]+")"
stop = stopwords.words('english')
sentence = res[0]["abstract"]
wo=set([stemmer.stem(i.replace(".","").replace(".","").replace(",","").replace("!","").replace(",","").replace("-","").replace(";","").replace('"',"").replace("'","").replace(":","").replace("?","").lower().decode("utf-8")) for i in sentence.split() if i.lower() not in stop])
res1=list(db.search_results.find({"query":query,"search_engine":{"$ne":"duckduckgo"}},{"snippet":1,"_id":0}))
wi=set()
wi=wi.union(wo)
for i in res1:
	i["snippet"]=i["snippet"].lower().replace(".","").replace(",","").replace("!","").replace(",","").replace("-","").replace(";","").replace('"',"").replace("'","").replace(":","").replace("?","")
	temp=set([filter(lambda x:ord(x)>31 and ord(x)<128,i) for i in i["snippet"].split() if i.lower() not in stop])
	wi=temp.union(wi)
final=set()
for i in wi:
	try:
		i=stemmer.stem(i.decode('utf8'))
		if d.check(i)==True:
			if query not in i and not i.isdigit():
				final.add(i)
	except:
		pass
print "Query Expanded"
for i in final:
	print query+" "+i
