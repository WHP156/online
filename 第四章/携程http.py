import asyncio
import aiohttp
urls=[
    'https://i1.huishahe.com/uploads/tu/201911/9999/766d82b8a0.jpg',
    'https://i1.huishahe.com/uploads/tu/201911/9999/1667531d61.jpg',
    'https://i1.huishahe.com/uploads/tu/201911/9999/d0fcb718a2.jpg'
]
async def aiodownload(url):
    name=url.split('/')[-1]
    async with aiohttp.ClientSession() as r:#<==>requests模块
        async with r.get(url) as resp:
            #可以用aiofiles进行
            with open(f'online/第四章/美女图片/{name}.jpg',mode='wb') as f:
                f.write(await resp.content.read())
async def main():
    tasks=[asyncio.create_task(aiodownload(url)) for url in urls]
    await asyncio.wait(tasks)
if __name__ == "__main__":
    asyncio.run(main())
    print('over')