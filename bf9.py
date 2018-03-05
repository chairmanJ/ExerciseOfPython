from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages=set()
def getLinks(pageUrl):
    global pages
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj=BeautifulSoup(html,"html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("页面缺少一些属性！but don't worry")
    
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #遇到新页面
                newpage=link.attrs['href']
                print("--------------\n"+newpage)
                pages.add(newpage)
                getLinks(newpage)

getLinks("")



