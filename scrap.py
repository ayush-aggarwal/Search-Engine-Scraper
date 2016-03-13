import os
import result_parse
import aol_scrape
import ask_scrap
import pymongo
client=pymongo.MongoClient()
db=client.text_mining
db.search_results.remove({})
print("\n\nWelcome to the Scraping Results from Search Engines")
query=input("\nPlease Enter Query:- ")
pages=input("\nPlease enter the number of pages:- ")
se=input("\nPlease Enter Search Engines you want to scrap seprated by comma :- ")
se=se.replace(" ","")
if "aol" in se:
	print("Scraping from aol.com")
	aol_scrape.aol(query,pages)
	se=se.replace(",aol","").replace("aol,","").replace("aol","")
if "ask" in se:
	print("Scraping from ask.com")
	ask_scrap.ask(query,pages)
	se=se.replace(",ask","").replace("ask,","").replace("ask","")
if len(se.strip())!=0:
	fname=input("\nPlease Enter Output File Name:- ")
	fname=fname+".json"
	cmd="GoogleScraper -m http -q '"+query+"' --output-filename "+fname+" -s "+se+" -p "+pages
	print (cmd)
	print (os.popen(cmd).read())
	result_parse.parse(fname)
result_parse.duckduckgo(query)
	
