#
#
#TASK1
# import time
#
# def fun1(x):
#     print('Start fun1...')
#     print(f'x ** 2 = {x**2}')
#     print('fun1 sleep')
#     time.sleep(3)
#     print('...fun1 wake up and finished')
#
# def fun2(x):
#     print('Start fun2...')
#     print(f'x**0.5 = {x**0.5}')
#     print('fun2 sleep')
#     time.sleep(3)
#     print('...fun2 wake up and finished')
#
# def main():
#     fun1(4)
#     fun2(4)
#
# print(time.strftime('%X'),':programm started')
#
# main()
#
# print(time.strftime('%X'),':programm finished')
#
#TASK2
# #
# import asyncio
# import time
#
#
# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 finished')
#
# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 finished')
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#
#     await task1
#     await task2
#
#
# print(time.strftime('%X'))
#
# asyncio.run(main())
#
# print(time.strftime('%X'))

# TASK3
#
# import asyncio
# import time
#
# async def fun1(x):
#     print(x ** 2)
#     await asyncio.sleep(3)
#     print('fun1 finished')
#
# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 finished')
#
# print(time.strftime('%X'))
#
# loop = asyncio.get_event_loop()
# task1 = loop.create_task(fun1(4))
# task2 = loop.create_task(fun2(4))
# loop.run_until_complete(asyncio.wait([task1, task2]))
#
# print(time.strftime('%X'))


#TASK4

# import asyncio
# import time
#
# async def fun1(x):
#     print(x**2)
#     time.sleep(3)
#     print('fun1 finished')
#
# async def fun2(x):
#     print(x**0.5)
#     time.sleep(3)
#     print('fun2 finished')
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#
#     await task1
#     await task2
#
# print(time.strftime('%X'))
#
# asyncio.run(main())
#
# print(time.strftime('%X'))

#TASK 5

# import asyncio
#
# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 finished')
#
# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 finished')
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#
#     print(type(task1))
#     print(task1.__class__.__bases__)
#
#     await task1
#     await task2
#
# asyncio.run(main())
#
#TASK 6

# def fun1(x):
#     print(x**2)
#     sleep(3)
#     print('fun1 finished')
#
# def fun2(x):
#     print(x**0.5)
#     sleep(3)
#     print('fun2 finished')
#
# def main():
#     task1 = create_task(fun1(4))
#     task2 = create_task(fun2(4))
#
#     task1
#     task2
#
#
# main()

#TASK7

# import asyncio
# import time
#
#
# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 finished')
#
# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 finished')
#
# async def main():
#     await fun1(4)
#     await fun2(4)
#
#
# print(time.strftime('%X'))
#
# asyncio.run(main())
#
# print(time.strftime('%X'))

#TASK7

import time
import requests

