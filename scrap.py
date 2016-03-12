import os
import result_parse
print("\n\nWelcome to the Scraping Results from Search Engines")
query=input("\nPlease Enter Query:- ")
se=input("\nPlease Enter Search Engines you want to scrap seprated by comma :- ")
se=se.replace(" ","")
fname=input("\nPlease Enter Output File Name:- ")
fname=fname+".json"
pages=input("\nPlease enter the number of pages:- ")
cmd="GoogleScraper -m http -q '"+query+"' --output-filename "+fname+" -s "+se+" -p "+pages
print (cmd)
print (os.popen(cmd).read())
result_parse.parse(fname)
result_parse.duckduckgo(query)
