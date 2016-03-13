# Search-Engine-Scraper
This is the scraper which scraps data from various search engines and parses the data and parses it into required format.
This uses GoogleScraper so it requires the  following commands

Installation
1. sudo su
2. virtualenv --python python3 env
3. source env/bin/activate
4. pip install GoogleScraper

After installation check whether it is installed by:-
GoogleScraper -h
After that clone the repo and run the following command:- 
1. source env/bin/activate
2. python scrap.py
3. Check the results in mongodb

Search Engines Supported:-
1. Google
2. Bing
3. Yandex
4. Baidu
5. AOL
6. Duckduckgo
