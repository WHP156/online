import requests
from lxml import etree
url='https://www.zbj.com/fw/?k=saas'
resp=requests.get(url)
html=etree.HTML(resp.text)
divs=html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div')
for div in divs:
    price =div.xpath(".//div[@class='price']/span/text()")[0].strip('¥')
    name='saas'.join(div.xpath(".//div[@class='name-pic-box']/a/span/text()"))
    print(name,price)
resp.close()