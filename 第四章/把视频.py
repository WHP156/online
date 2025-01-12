 #通常放在M3U里，经过utf-8编码成M3U8，包含加密的key
import requests
import re
import aiofiles
# url='https://www.kkghg.com/play/23629-1-0.html'
# main_resp=requests.get(url)
# obj=re.compile(r'var now="(?P<url>.*?)";',re.S)#提取地址
# s=obj.search(main_resp.text)
# m3u8_url=s.group('url')
# main_resp.close()
# m3u8_list=m3u8_url.split('/')
# m3u8_list.insert(-1,'1000k')
# m3u8_list.insert(-1,'hls')
# m3u8_url='/'.join(m3u8_list)
# m3u8_resp=requests.get(m3u8_url)
# with open('一个好汉.m3u8',mode='wb') as f:
#     f.write(m3u8_resp.content)
# #https://yzzy.play-cdn12.com/20221212/9906_b16cb9d6/1000k/hls/index.m3u8
# #https://yzzy.play-cdn12.com/20221212/9906_b16cb9d6/index.m3u8
# m3u8_resp.close()
#有m3u8后其余都可以不要了
n=0
mainurl='https://yzzy.play-cdn12.com/20221212/9906_b16cb9d6/1000k/hls/'
with open('一个好汉.m3u8',mode='r',encoding='utf-8') as f:
    for line in f:
        line=line.strip()#去掉空白，换行符之类的
        if line.startswith('#'):
            continue
        line=mainurl+line
        resp3=requests.get(line)
        f1=open(f'online/第四章/一个好汉/{n}.ts',mode='wb')
        f1.write(resp3.content)
        n+=1
        f1.close()
        print('over')