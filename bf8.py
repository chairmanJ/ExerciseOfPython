from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages=set()
def getLinks(pageUrl):
    global pages
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj=BeautifulSoup(html)
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs["href"] not in pages:
                #遇到新页面
                newpage=link.attrs["href"]
                print(newpage)
                pages.add(newpage)
                getLinks(newpage)

getLinks("")
