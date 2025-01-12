import requests
url='https://m.po18gg.com/login.php'
data={
    '_17mb_username':'wang',
    '_17mb_password':'wanghaopu'
}
session=requests.session()
resp=session.post(url,data=data)
resp1=session.get('https://m.po18gg.com/')
#resp1=requests.get('https://m.po18gg.com/')
print(resp1.text)
resp.close()
resp1.close()
