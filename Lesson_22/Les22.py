

# import asyncio
#
# async def async_func():
#     print('Start...')
#     await asyncio.sleep(1)
#     print('...Ready')
#
# async def main():
#     # async_func()
#     await async_func()
#
#
#
# asyncio.run(main())


# import asyncio
#
# async def async_func(task_no):
#     print(f'{task_no}: Start...')
#     await asyncio.sleep(1)
#     print(f'{task_no}...Ready')
#
#
# async def main():
#     taskA = loop.create_task(async_func('taskA'))
#     taskB = loop.create_task(async_func('taskB'))
#     taskC = loop.create_task(async_func('taskC'))
#     await asyncio.wait([taskA,taskB,taskC])
#
# if __name__ == "__main__":
#     try:
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(main())
#     except:
#         pass

#
# import asyncio
# import time
# from aiohttp import ClientSession
#
# async def fetch_url_data(session,url):
#     try:
#         async with session.get(url,timeout=60) as response:
#             resp = await response.read()
#     except Exception as e:
#         print(e)
#     else:
#         return resp
#     return
#
# async def fetch_async(loop,r):
#     url = "https://www.uefa.com/uefaeuro-2020/"
#     tasks = []
#     async with ClientSession() as session:
#         for i in range(r):
#             task = asyncio.ensure_future(fetch_url_data(session,url))
#             tasks.append(task)
#         responses = await asyncio.gather(*tasks)
#     return responses
#
# if __name__ == '__main__':
#     for ntimes in [1,10,50,100,500]:
#         start_time = time.time()
#         loop = asyncio.get_event_loop()
#         future = asyncio.ensure_future(fetch_async(loop, ntimes))
#         loop.run_until_complete(future)
#         responses = future.result()
#         print(f'Get {ntimes} results of request for {time.time() - start_time} seconds')


# import threading
# import time
# import random
#
# def worker(number):
#     sleep = random.randrange(1,10)
#     time.sleep(sleep)
#     print('I am worker {}, I slept for {} seconds'.format(number,sleep))
#
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     t.start()
#
# print("All Threads are queued, let's see when they finish!")


# from threading import Thread
# from time import sleep
#
# class CustomThread(Thread):
#     def __init__(self,limit):
#         Thread.__init__(self)
#         self._limit = limit
#
#     def run(self):
#         for i in range(self._limit):
#             print(f"from CustomThread: {i}")
#             sleep(0.5)
#
# cth = CustomThread(3)
# cth.start()
#
# from threading import Thread
# from time import sleep
#
# def func():
#     for i in range(5):
#         print(f"from child thread: {i}")
#         sleep(0.5)
#
# th=Thread(target=func, daemon=True)
# th.start()
# print('App stop')


