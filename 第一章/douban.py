import requests as r 
url='https://movie.douban.com/j/chart/top_list?'
param={
    'type': '24',
    'interval_id' :"100:90",
    'action': '',
    'start': '0',
    'limit': '20', 
}
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
resp=r.get(url,params=param,headers=headers)
print(resp.json())
resp.close()