import requests
from bs4 import BeautifulSoup
import pandas


class getNews:
    def __init__(self):
        self.d={}

    def get_news_from_toi(self):
        i=1
        url='https://timesofindia.indiatimes.com/news/'
        while i<=8:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            news=soup.select('#ulItemContainer ul li a')
            for n in news:
                try:
                    self.d['https://m.timesofindia.com'+n['href']]=n['title']
                except:
                    pass
            i=i+1
            url=url+'/'+str(i)
        
    def get_news_from_ndtv(self):
        i=1
        url='https://www.ndtv.com/latest/'
        while i<=8:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            news=soup.select('.lisingNews .news_Itm .news_Itm-cont h2 a')
            for n in news:
                try:
                    self.d[n['href']]=n.text
                except:
                    pass
            i=i+1
            url=url+'/page-'+str(i)
    
    def get_dataframe(self):
        return pandas.DataFrame(self.d.items(), columns=['HeaderUrl','HeaderName'])
    
# o=getNews()
# o.get_news_from_ndtv()
# o.get_news_from_toi()
# print(o.get_dataframe())

