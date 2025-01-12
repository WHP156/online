import re
list=re.findall(r'\d+','my phone number is 10086,10010')
it=re.finditer(r'\d+','my phone number is 10086,10010')
for i in it:
    print(i.group())
s=re.search(r'\d+','my phone number is 10086,10010')
# 会报错m=re.match(r'\d+'(#相当于^\d+),'my phone number is 10086,10010')
print(s.group())
obj=re.compile(r'\d+')#预加载
m=obj.match('10030,my phone number is 10086,10010')
print(m.group())
s1="""
我的手机号：123，
他的手机号：456，
你的手机号：789，
我们的手机号：123456789，
"""
obj1=re.compile('(?P<name>.*?)的手机号：(?P<number>.*?)，',re.S)#re.S可以让*匹配everything
result=obj1.finditer(s1)
for i in result:
    print(i.group('name'))
    print(i.group('number'))