import aiohttp
import asyncio
import time

start = time.time()


# async def get(url):
#     session = aiohttp.ClientSession()         # 实例化Clientsession()对象
#     response = await session.get(url)         # 支持get(),post()，params/data,proxy='..'等参数
#     result = await response.text()            # text()字符串，json()json类型，read()二进制
#     await session.close()                     # 关闭资源，使用with语句可以自动释放
#     return result


async def get_w(rul):
    async with aiohttp.ClientSession() as session:
        async with await  session.get(rul) as response:
            result = await response.text()
            return result


async def request():
    url = 'http://127.0.0.1:5000'
    print('Waiting fro ', url)
    # result = await get(url)
    result = await get_w(url)
    print('Get response from ', url, 'Result:', result)


tasks = [asyncio.ensure_future(request()) for _ in range(5)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)
