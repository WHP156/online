import requests
name=input('Anything you want')
url=f'https://www.sogou.com/web?query={name}'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
resp=requests.get(url,headers=headers)
print(resp.text)
resp.close()