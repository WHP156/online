import requests
import re
import asyncio
import aiofiles
import aiohttp
import os#命令
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
def get1m3u8(url):
    main_resp=requests.get(url,headers=headers)
    obj=re.compile(r"% src='(?P<url>.*?)'",re.S)
    m3u8_url=obj.search(main_resp.text).group('url')
    main_resp.close()
    m3u8_url=m3u8_url[m3u8_url.find('=')+1:]
    return m3u8_url
def get2m3u8(url):
    m3u8_resp=requests.get(url)
    m3u8=m3u8_resp.text
    m3u8_resp.close()
    return m3u8
def absm3u8(m1,m2):
    add=m2.split('\n')[2]
    new=m1.replace('index.m3u8',add)
    return new
def downloadfile(url,name):
    url1=url.strip()#一定要有strip（）
    resp1=requests.get(url1)
    with open(name,mode='wb') as f:
        f.write(resp1.content)
    resp1.close()
async def downloadts(url,session,i):
        async with session.get(url) as resp:
            async with aiofiles.open(f'online/第四章/夏洛特/{i}.ts',mode='wb') as f:
                content=await resp.read()
                await f.write(content)
            print(f'{url}下载over')
async def aio_downloads():
    i=0
    tasks=[]
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open('good.m3u8',mode='r',encoding='utf-8') as f:
            async for line in f:
                if line.startswith('#'):
                    continue
                else :
                    line=line.strip()
                task=asyncio.create_task(downloadts(line,session,i))
                tasks.append(task)
                i+=1
            await asyncio.wait(tasks)
def merge_ts():

    lst=[f"{i}.ts" for i in range(0,2643)]
    s=" + ".join(lst)#可以合并，但会出现命令行太长的问题
    s=f'cd C:/Users/1/Desktop/python try/online/第四章/夏洛特 \n'+'copy /b '+s+' charlot.mp4'
    #如果直接*.ts会由于顺序不对而无法观看，
    #可用ffmpeg解决，也可用bat文件
    with open('online\第四章\夏洛特\合并.bat',mode='w') as f:
        f.write(s)
    #os.system(f"online\第四章\夏洛特\合并.bat")直接用貌似会死机
    print('over')

def main(url):
     m1=get1m3u8(url)
     m2=get2m3u8(m1)
     m3=absm3u8(m1,m2)
     downloadfile(m3,'good.m3u8')
     asyncio.run(aio_downloads())

if __name__ == "__main__":
    url='http://www.mjtt1.cc/p/423516/264/1375433'
    main(url)
    merge_ts()