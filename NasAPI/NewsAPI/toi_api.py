import requests
from bs4 import BeautifulSoup
import pandas


class getNewsFromToi:
    def get_news_from_toi(self):
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
        return pandas.DataFrame(d.items(), columns=['HeaderUrl','HeaderName'])
    

# o=getNews()
# print(o.get_news_from_toi())

        
    
