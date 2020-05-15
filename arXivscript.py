# Python script to display new articles from arXiv
#   run: python arXivscript.py 'subject'

import sys
import requests
from bs4 import BeautifulSoup

SUBJECT = sys.argv[1] #'math.PR'
URL = 'https://arxiv.org/list/' + SUBJECT + '/new'

# Prints only the SUBJECT New articles, not Crossposts
def create_pretty_listing(entry_header,entry):
    result = ''
    result += entry_header.find(title="Abstract").text + '\n'
    result += "Link --> https://arxiv.org/abs/" + entry_header.find(title="Abstract").text[6:]
    result += entry.find("div", {"class": "list-title mathjax"}).text
    result += entry.find("div", {"class": "list-authors"}).text  + '\n'
    result += entry.find("p").text
    # Comments section not required by arXiv
    if entry.find("div", {"class": "list-comments mathjax"}) != None:
        result += entry.find("div", {"class": "list-comments mathjax"}).text 
    if entry.find("div", {"class": "list-subjects"}) != None:
        result += entry.find("div", {"class": "list-subjects"}).text
    result += '\n'*2
    return result

page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')
content = soup.dl 

listings_headers = content.find_all('dt')
listings = content.find_all('dd')
print('\n\nFound {} new postings in {}...\n\n'.format(len(listings),SUBJECT))
for i in range(len(listings)):
    print(create_pretty_listing(listings_headers[i],listings[i]))