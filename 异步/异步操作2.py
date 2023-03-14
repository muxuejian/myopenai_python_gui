from queue import Queue
import asyncio

# 如何在主题q队列有限的情况下如何进行，取存
'''
问题：
    无法进行多个消费者携程操作或者做起来很麻烦需要更优解，并且单个消费者不如做成同步

需要解决问题：
    如何解决Q队列在有限的空间，无限的插入，进行挂起的情况
    
解决方案：
    使用put_nowait 或timeout超时进行解决并捕获异常
    
新问题：
    

'''
#生产者
async def scz(q):
    number = 0
    while True:
        if q.full():
            await xfz1(q)
        else:
            print('生产数字%s'%number)
            number = number+1
            q.put(number)


#消费者
async def xfz1(q):
    if not q.empty():
        response = q.get()
        print('消费1数字%s'%response)
    else:
        await scz(q)
    return response

#消费者
async def xfz2(q):
    if not q.empty():
        response = q.get()
        print('消费2数字%s'%response)
    else:
        await scz(q)
    return response

#主方法
async def main():
    q = Queue(3)
    asyncio.create_task(scz(q))
    asyncio.create_task(xfz1(q))
    asyncio.create_task(xfz2(q))

if __name__ == '__main__':
    asyncio.run(main())

