import requests
from bs4 import BeautifulSoup
import pandas

class getNewsFromAbp:
    def get_news_from_abp(self):
        url='https://news.abplive.com/latest-news'
        i=1
        d={}
        while i<=8:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            news=soup.select('.other_news a')
            for n in news:
                try:
                    d[n['href']]=n['title']
                except:
                    pass
            i=i+1
            url=url+'/page-'+str(i)

        return pandas.DataFrame(d.items(), columns=['HeaderUrl','HeaderName'])
    
# o=getNews()
# print(o.get_news_from_abp())
        
