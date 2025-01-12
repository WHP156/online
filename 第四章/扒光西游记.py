import requests
import asyncio
import aiohttp
import aiofiles
import json
url='https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
urls='https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}'
b_id='4306063500'
refer='https://dushu.baidu.com/pc/reader?gid=4306063500&cid='
head={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'cookies':'BAIDUID_BFESS=E57EF0F1E8F568F1DB3E4AAA20B2FEED:FG=1; BIDUPSID=E57EF0F1E8F568F1DB3E4AAA20B2FEED; PSTM=1734615942; H_PS_PSSID=61027_61244_61371_61390_61427_61434_61445_61465_60853; ZFY=cKKI3XULhTulIQeicFjvfVnGYJ9HRY2pOo8kCUbgTBs:C; __bid_n=193f944e5d79552283c95b; ariaDefaultTheme=undefined; Hm_lvt_bf1e478a71b02a743ab42bcfed9d1ff1=1735736661,1735799460; HMACCOUNT=24422B0924ED7AB3; Hm_lpvt_bf1e478a71b02a743ab42bcfed9d1ff1=1735799584',
    'referer':'https://dushu.baidu.com/pc/reader?gid=4306063500&cid='
    }
async def aiodownload(cid,b_id,title):
    data={
        "book_id":"4306063500",
        "cid":b_id+'|'+cid,
        "need_bookinfo":1
    }
    data=json.dumps(data)
    now_url=f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    head['referer']+=cid
    async with aiohttp.ClientSession() as r:
        async with r.get(now_url,headers=head) as resp:
            dic1=await resp.json()
            async with aiofiles.open('online/第四章/西游记/'+title,mode='w',encoding='utf-8') as f:
                await f.write(dic1['data']['novel']['content'])
async def getcatelog(url):
    resp=requests.get(url)
    dic=resp.json()
    tasks=[]
    for item in dic['data']['novel']['items']:
        title=item['title']
        cid=item['cid']
        tasks.append(asyncio.create_task(aiodownload(cid,b_id,title)))
        await asyncio.wait(tasks)
if __name__ == "__main__":
    asyncio.run(getcatelog(url))