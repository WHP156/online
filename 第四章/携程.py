import time
# def func():
#     print(1)
#     time.sleep(3)#可以CPU干其他的事
#     print(2)
# if __name__ == "__main__":
#     func()
#单线程,多任务


import asyncio
async def func():
    print(12)
    #time.sleep(3)对async没有影响requests.get()也是，要改成异步操作的代码
    await asyncio.sleep(3)
    print(12)
async def func1():
    print(1)
    #time.sleep(5)
    await asyncio.sleep(5)
    print(1)
async def func2():
    print(23)
    #time.sleep(2)
    await asyncio.sleep(2)
    print(23)
#if __name__ == "__main__":
    # g=func()
    # g1=func1()
    # g2=func2()
    # loop=asyncio.new_event_loop()
    # tasks=[
    #     loop.create_task(i) for i in [g,g1,g2]
    # ]
    # t1=time.time()
    # loop.run_until_complete(asyncio.wait(tasks))
    # t2=time.time()
    # print(t2-t1)
async def main():
    task1=asyncio.create_task(func())
    task2=asyncio.create_task(func1())
    result1=await task1
    result2=await task2
    return result1,result2
if __name__ == "__main__":
    asyncio.run(main())