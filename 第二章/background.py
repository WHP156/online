import requests
from bs4 import BeautifulSoup
import time
url='https://www.umeituku.com/bizhitupian/weimeibizhi/'
resp=requests.get(url)
resp.encoding='utf-8'
main_page=BeautifulSoup(resp.text,'html.parser')
typelist=main_page.find('div',class_='TypeList')
hrefs=typelist.find_all('a')
for it in hrefs:
    sub_url=it.get('href')
    sub_resp=requests.get(sub_url)
    sub_resp.encoding='utf-8'
    sub_page=BeautifulSoup(sub_resp.text,'html.parser')
    img=sub_page.find('div',class_='ImageBody').find('img')
    download=img.get('src')
    name=img.get('alt')
    img_resp=requests.get(download)
    with open('online/第二章/背景图片/'+name+'.jpg',mode='wb') as f:
        f.write(img_resp.content)
    print(name,'over')
    time.sleep(2)
    sub_resp.close()
resp.close()