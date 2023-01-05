import asyncio
from async_learn import delay


async def main(n: int, m: int):

    # sleep_1 = asyncio.create_task(delay(n))
    # sleep_2 = asyncio.create_task(delay(n))
    # sleep_3 = asyncio.create_task(delay(n))

    # await sleep_1
    # await sleep_2
    # await sleep_3

    tasks = []
    for i in range(m):
        task = asyncio.create_task(delay(n))
        tasks.append(task)

    for i in tasks:
        await i

    print('lalala')

asyncio.run(main(5, 3))

