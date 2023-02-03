import asyncio #  [1]
import aiohttp
# async def main(): # [2]
#     async with aiohttp.ClientSession() as session: # [3]
#         async with session.get('http://example.com') as resp: # [4]
#             response = await resp.read() # [5]
#             print(response)
# asyncio.run(main()) # [6]



async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://example.com',
            headers={'Authorization':'Bearer 123456', 'Content-Type':'application/json'},
            json={'title':'Try Bearer'}) as resp: # [1]
            response = await resp.json(encoding='UTF-8')# [2]
            print(response)
asyncio.run(main())


