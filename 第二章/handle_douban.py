import re
import requests
import csv
url='https://movie.douban.com/chart'
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
resp=requests.get(url,headers=headers)
page_content=resp.text
obj=re.compile(r'<p class="ul.*?"></p>.*?title="(?P<name>.*?)">.*?<p class="pl">(?P<year>.*?)/'
               r'.*?<span class="pl">(?P<score>.*?)</span>',re.S)
it=obj.finditer(page_content)
f=open('dourank.csv',mode='w',encoding='utf-8')
w=csv.writer(f)
for i in it:
    dic=i.groupdict()
    w.writerow(dic.values())
f.close()
resp.close()
print('over')
