import re
import requests
domain='https://www.dy2018.com/'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
do_resp=requests.get(domain,headers=headers,verify=False)
do_resp.encoding='gb2312'
obj=re.compile(r'2024必看热片</span>.*?<ul>(?P<ul>.*?)</ul>',re.S)
result1=obj.finditer(do_resp.text)
obj1=re.compile(r"<a href='(?P<href>.*?)'",)
childhreflist=[]
obj2=re.compile(r'片　　名　(?P<name>.*?)<br />.*?'
                r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<href>.*?)">magnet',re.S)
for it in result1:
    ul=it.group('ul')
    result2=obj1.finditer(ul)
    for i in result2:
        childhref=domain+i.group('href').strip('/')
        childhreflist.append(childhref)
for href in childhreflist:
    sub_resp=requests.get(href,verify=False,headers=headers)
    sub_resp.encoding='gb2312'
    result3=obj2.finditer(sub_resp.text)
    for i in result3:
        print(i.group('name'))
        print(i.group('href'))
    sub_resp.close()
do_resp.close()