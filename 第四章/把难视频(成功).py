import requests
import re
import asyncio
import aiofiles
import aiohttp
import os#命令
#有一个缺陷，下载到某些地点不是很稳定，不能自动刷新
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
def get1m3u8(url):
    main_resp=requests.get(url,headers=headers)
    obj=re.compile(r"% src='(?P<url>.*?)'",re.S)
    m3u8_url=obj.search(main_resp.text).group('url')
    main_resp.close()
    m3u8_url=m3u8_url[m3u8_url.find('=')+1:]
    print('first over')
    return m3u8_url
def get2m3u8(url):
    m3u8_resp=requests.get(url,headers=headers)
    m3u8=m3u8_resp.text
    m3u8_resp.close()
    print('second over')
    return m3u8
def absm3u8(m1,m2):
    add=m2.split('\n')[2]
    new=m1.replace('index.m3u8',add)
    print('combine over')
    return new
def downloadfile(url,name):
    url1=url.strip()#一定要有strip（）
    resp1=requests.get(url1,headers=headers)
    with open(name,mode='wb') as f:
        f.write(resp1.content)
    resp1.close()
    print('download over')
async def downloadts(url,session,i,name,episode):
        async with session.get(url,headers=headers) as resp:
            async with aiofiles.open(f'online/第四章/{name}/{episode}/{i}.ts',mode='wb') as f:
                content=await resp.read()
                await f.write(content)
            print(f'{url.split('/')[-1]}下载over')
async def aio_downloads(name,episode):
    tasks=[]
    i=0
    async with aiohttp.ClientSession() as session:
        s=name+str(episode)
        async with aiofiles.open(f'{s}.m3u8',mode='r',encoding='utf-8') as f:
            async for line in f:
                if line.startswith('#'):
                    continue
                else :
                    line=line.strip()
                task=asyncio.create_task(downloadts(line,session,i,name,episode))
                tasks.append(task)
                i+=1
            await asyncio.wait(tasks)
def merge_ts(num,name,episode):

    lst=[f"{i}.ts" for i in range(0,num)]
    s=" + ".join(lst)#可以合并，但会出现命令行太长的问题
    s=f'cd C:/Users/1/Desktop/python try/online/第四章/{name}/{episode} \n'+'copy /b '+s+f' {name}.mp4'
    #如果直接*.ts会由于顺序不对而无法观看
    with open(f'online/第四章/{name}/{episode}/合并.bat',mode='w') as f:
        f.write(s)
    #os.system(f"online\第四章\name\合并.bat")直接用貌似会死机
    print('over')
def get_num(name):
    i=0
    with open(f'{name}.m3u8',mode='r',encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else :
                i+=1
    return i
def geturl(main_url):
    resp=requests.get(main_url,headers=headers)
    obj=re.compile(r'&nbsp;免费云.*?</ul>',re.S)
    bigpart=obj.search(resp.text).group()
    resp.close()
    obj1=re.compile(r'<a href="(?P<url>.*?)" class="hide">')
    url_list=obj1.finditer(bigpart)
    urls=[]
    for url in url_list:
        url=url.group('url')
        url=main_url.split('/v')[0]+url
        urls.append(url)
    print('urls over')
    return urls
def create_dir(name,num):
    for i in range(1,num+1):
        os.makedirs(f'online/第四章/{name}/{i}')
        print("sub dirs over")
def want():
    name=input("请输入你想要下载的美剧:")
    preurl='https://www.mjtt1.cc/public/auto/search1.html?keyword='
    url=preurl+name
    second_url=''
    with requests.get(url,headers=headers) as resp:
        resp.encoding='utf-8'
        obj=re.compile(r'<div class="public-list-button">.*?<a href="(?P<url>.*?)"',re.S)
        second_url=obj.search(resp.text).group('url')
    url=preurl.split('/public')[0]+second_url
    os.makedirs(f'online/第四章/{name}')
    return url,name
def main():
     main_url,name=want()
     name='t'
     url_list=geturl(main_url)
     num_episode=len(url_list)
     create_dir(name,num_episode)
     episode=1
     for url in url_list:
        print(f'the {episode} begin')
        m1=get1m3u8(url)
        m2=get2m3u8(m1)
        m3=absm3u8(m1,m2)
        downloadfile(m3,f'{name}{episode}.m3u8')
        asyncio.run(aio_downloads(name,episode))
        num=get_num(name+str(episode))
        merge_ts(num,name,episode)
        episode+=1
        print(f'the {episode} over')    
if __name__ == "__main__":
    main()