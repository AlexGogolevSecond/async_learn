import asyncio
from async_learn import delay


async def main():
    sleep_ = asyncio.create_task(delay(3))
    print(type(sleep_))
    res = await sleep_
    print(res)
    print('lalala')


asyncio.run(main())

