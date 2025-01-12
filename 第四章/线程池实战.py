import requests
import csv
from concurrent.futures import ThreadPoolExecutor
url='http://www.xinfadi.com.cn/getPriceData.html'
f=open('菜价.csv',mode='w',encoding='utf-8')
def get_data(number):
    data={
        'limit': '20',
        'current': f'{number}',
        'pubDateStartTime': '',
        'pubDateEndTime': '',
        'prodPcatid': '',
        'prodCatid': '',
        'prodName': ''
    }
    return data
def download_onepage(number):
    resp=requests.post(url=url,data=get_data(number))
    list=dict(resp.json())['list']
    resp.close()
    for it in list:
        line=it['prodName']+' '+it['avgPrice']+' '
        f.writelines(line+'\n') 
if __name__ == "__main__":
    with ThreadPoolExecutor(50) as t:
        for i in range(1,200):
            t.submit(download_onepage,i)
    f.close()
    print('over')
