import requests
from bs4 import BeautifulSoup
import csv
url='https://nba.hupu.com/standings'
resp=requests.get(url)
f=open("NBA排名",mode='w',encoding='utf-8')
w=csv.writer(f)
page=BeautifulSoup(resp.text,'html.parser')
table=page.find('table',class_="players_table")
#等价于table=page.find('table',attrs={'class':'xxxx'})
trs=table.find_all('tr')[2:]
for tr in trs:
    tds=tr.find_all('td')
    try:
        name=tds[1].text
        win=tds[2].text
        lost=tds[3].text
        rank=tds[0].text
        w.writerow([name,win,lost,rank])
    except IndexError or TypeError:
        print('error')
        continue
resp.close()
f.close()
print('over')
