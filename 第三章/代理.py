import requests
#121.8.215.106	9797	HTTP	透明	广东省广州市 电信
proxies={
    'https':'https://39.106.60.216:3128'
}
resp=requests.get('https://www.baidu.com',proxies=proxies)
resp.encoding='utf-8'
print(resp.text)
resp.close()