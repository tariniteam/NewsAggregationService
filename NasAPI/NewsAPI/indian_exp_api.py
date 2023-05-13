import requests
from bs4 import BeautifulSoup
import pandas


class getNewsFromIndianExpress:
    def get_news_from_indianExpress(self):
        url='https://indianexpress.com/latest-news/'
        i=1
        d={}
        while i<=8:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            news=soup.select('.articles .title a')
            for n in news:
                try:
                    d[n['href']]=n.text
                except:
                    pass
            i=i+1
            url=url+'/page/'+str(i)

        return pandas.DataFrame(d.items(), columns=['HeaderUrl','HeaderName'])
 
# o=getNews()
# print(o.get_news_from_indianExpress())
