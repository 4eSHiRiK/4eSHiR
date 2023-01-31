import asyncio



"""Потоки — наиболее распространённый инструмент. Думаю, вы слышали о нём и ранее, однако asyncio оперирует несколько другими понятиями: циклы событий, корутины и футуры.

цикл событий (event loop) по большей части всего лишь управляет выполнением различных задач: регистрирует поступление и запускает в подходящий момент
корутины — специальные функции, похожие на генераторы python, от которых ожидают (await), что они будут отдавать управление обратно в цикл событий. Необходимо, чтобы они были запущены именно через цикл событий
футуры — объекты, в которых хранится текущий результат выполнения какой-либо задачи. Это может быть информация о том, что задача ещё не обработана или уже полученный результат; а может быть вообще исключение"""

#task1
# async def foo():
#     print('Running in foo')
#     await asyncio.sleep(0)
#     print('Explicit context switch to foo again')
#
#
# async def bar():
#     print('Explicit context to bar')
#     await asyncio.sleep(0)
#     print('Implicit context switch back to bar')
#
#
# ioloop = asyncio.get_event_loop()
# tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
# wait_tasks = asyncio.wait(tasks)
# ioloop.run_until_complete(wait_tasks)
# ioloop.close()

#task2
# import time
# import asyncio
#
# start = time.time()
#
#
# def tic():
#     return 'at %1.1f seconds' % (time.time() - start)
#
#
# async def gr1():
#     # Busy waits for a second, but we don't want to stick around...
#     print('gr1 started work: {}'.format(tic()))
#     await asyncio.sleep(2)
#     print('gr1 ended work: {}'.format(tic()))
#
#
# async def gr2():
#     # Busy waits for a second, but we don't want to stick around...
#     print('gr2 started work: {}'.format(tic()))
#     await asyncio.sleep(2)
#     print('gr2 Ended work: {}'.format(tic()))
#
#
# async def gr3():
#     print("Let's do some stuff while the coroutines are blocked, {}".format(tic()))
#     await asyncio.sleep(1)
#     print("Done!")
#
#
# ioloop = asyncio.get_event_loop()
# tasks = [
#     ioloop.create_task(gr1()),
#     ioloop.create_task(gr2()),
#     ioloop.create_task(gr3())
# ]
# ioloop.run_until_complete(asyncio.wait(tasks))
# ioloop.close()

#task 3
from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def fetch_ip(service):
    start = time.time()
    print('Fetching IP from {}'.format(service.name))

    response = await aiohttp.request('GET', service.url)
    json_response = await response.json()
    ip = json_response[service.ip_attr]

    response.close()
    return '{} finished with result: {}, took: {:.2f} seconds'.format(
        service.name, ip, time.time() - start)


async def asynchronous():
    futures = [fetch_ip(service) for service in SERVICES]
    done, pending = await asyncio.wait(
        futures, return_when=FIRST_COMPLETED)

    print(done.pop().result())

    for future in pending:
        future.cancel()


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()