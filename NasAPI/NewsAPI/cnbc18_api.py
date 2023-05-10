import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://www.cnbctv18.com/"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
print(soup)
for i in reversed(soup.find_all('a', class_='media__link')): 
    print(i)
    try :  
        href = i['href']
        if href[0]!='h':
            href = 'https://www.cnbctv18.com'+href
        
    except Exception as e:
        print("Error : ", e)
       