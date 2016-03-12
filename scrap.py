import os
import result_parse
import aol_scrape
f=0
print("\n\nWelcome to the Scraping Results from Search Engines")
query=input("\nPlease Enter Query:- ")
se=input("\nPlease Enter Search Engines you want to scrap seprated by comma :- ")
se=se.replace(" ","")
if "aol" in se:
	f=1
	se=se.replace(",aol","").replace("aol","").replace("aol","")
pages=input("\nPlease enter the number of pages:- ")
if len(se.strip())!=0:
	fname=input("\nPlease Enter Output File Name:- ")
	fname=fname+".json"
	cmd="GoogleScraper -m http -q '"+query+"' --output-filename "+fname+" -s "+se+" -p "+pages
	print (cmd)
	print (os.popen(cmd).read())
	result_parse.parse(fname)
result_parse.duckduckgo(query)
if f==1:
	aol_scrape.aol(query,pages)
