import time
import asyncio
async def download(url):
    print('begin')
    await asyncio.sleep(2)#换成requests的asyncio的模式函数
    print('over')
async def  main():
    urls=[
        'htttp',
        'hddp',
        'baidu'
    ]
    tasks=[]
    for url in urls:
        d=download(url)
        task=asyncio.create_task(d)
        tasks.append(task)
    await asyncio.wait(tasks)
if __name__ == "__main__":
    asyncio.run(main())