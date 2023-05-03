# from queue import Queue
# import asyncio
#
#
#
# #如何在主题q队列有限的情况下如何进行，取存
# '''
#
# 需要解决问题：
#     如何解决Q队列在有限的空间，无限的插入，进行挂起的情况(解决)
#
# '''
# #生产者
# async def scz(q):
#     number = 0
#     while True:
#         if q.full():
#             await xfz1(q)
#             await xfz2(q)
#         else:
#             print('生产数字%s' % number)
#             q.put(number)
#             number = number + 1
#
#
#
# #消费者
# async def xfz1(q):
#     if not q.empty():
#         response = q.get()
#         print('消费数字一%s'%response)
#         await asyncio.sleep(1)
#     else:
#         await scz(q)
#     return response
#
# #消费者
# async def xfz2(q):
#     if not q.empty():
#         response = q.get()
#         print('消费数字二%s'%response)
#     else:
#         await scz(q)
#     return response
#
# #主方法
# async def main():
#     q = Queue(3)
#     asyncio.create_task(scz(q))
#     asyncio.create_task(xfz1(q))
#     asyncio.create_task(xfz2(q))
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


#
# import asyncio
# from asyncio import Queue
#
# #创建一个生产者
# async def producer(queue):
#     while True:
#         #生产者生产数据
#         data = 'data'
#         #将数据放入队列
#         await queue.put(data)
#         print('Producer1 produced data: %s' %data)
#         await asyncio.sleep(1)
#
# #创建消费者
# async def consumer(queue):
#     while True:
#         #从队列中获取数据
#         data = await queue.get()
#         print('Consumer1 consumed data: %s' %data)
#         await asyncio.sleep(1)
#
# #创建事件循环
# async def main():
#     #创建队列
#     queue = Queue(maxsize=3)
#
#     #创建生产者任务
#     producer_task = asyncio.create_task(producer(queue))
#     #创建两个消费者任务
#     consumer_task1 = asyncio.create_task(consumer(queue))
#     consumer_task2 = asyncio.create_task(consumer(queue))
# #等待任务完成
#     await asyncio.gather(producer_task, consumer_task1, consumer_task2)
#
# if __name__ == '__main__':
#     asyncio.run(main())



#如何在主题q队列有限的情况下如何进行，取存
# '''
#
# 需要解决问题：
#     如何解决Q队列在有限的空间，无限的插入，进行挂起的情况(已解决：使用 asyncio 中的 import Queue)
#
# '''

#



import asyncio
from asyncio import Queue
# from queue import Queue（方法）

#生产者
async def scz(q):
    number = 0
    while True:
        print('生产数字%s' % number)
        await q.put(number)
        number = number + 1
        await asyncio.sleep(2)



#消费者
async def xfz1(q):
    while True:
        response = await q.get()
        print('消费数字一%s'%response)
        await asyncio.sleep(5)

#消费者
async def xfz2(q):
    while True:
        response = await q.get()
        print('消费数字二%s'%response)
        await asyncio.sleep(7)

#消费者
async def xfz3(q):
    while True:
        response = await q.get()
        print('消费数字三%s'%response)
        await asyncio.sleep(7)

#主方法
async def main():
    q = Queue(maxsize=3)
    producer_task = asyncio.create_task(scz(q))
    #创建两个消费者任务
    consumer_task1 = asyncio.create_task(xfz1(q))
    consumer_task2 = asyncio.create_task(xfz2(q))
    consumer_task3 = asyncio.create_task(xfz3(q))
    #等待任务完成
    await asyncio.gather(producer_task, consumer_task1, consumer_task2, consumer_task3)



if __name__ == '__main__':
    asyncio.run(main())
