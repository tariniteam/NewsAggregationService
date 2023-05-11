import requests
from bs4 import BeautifulSoup

def toi():
    url='https://timesofindia.indiatimes.com/news/'
    i=1
    d={}
    while i<=8:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        news=soup.select('#ulItemContainer ul li a')
        for n in news:
            try:
                d['https://m.timesofindia.com'+n['href']]=n['title']
            except:
                pass
        i=i+1
        url=url+'/'+str(i)
    return d

def ndtv():
    url='https://www.ndtv.com/latest/'
    i=1
    d={}
    while i<=8:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        news=soup.select('.lisingNews .news_Itm .news_Itm-cont h2 a')
        for n in news:
            try:
                d[n['href']]=n.text
            except:
                pass
        i=i+1
        url=url+'/page-'+str(i)
    return d

