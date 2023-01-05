import asyncio

from async_learn import delay

# from async_learn import delay


async def hello_():
    for i in range(2):
        await asyncio.sleep(1)
        print('pause 1 sec')


async def main(delay_sec: int, count_tasks: int):

    # region
    # sleep_1 = asyncio.create_task(delay(n))
    # sleep_2 = asyncio.create_task(delay(n))
    # sleep_3 = asyncio.create_task(delay(n))
    #
    # await sleep_1
    # await sleep_2
    # await sleep_3
    # endregion

    tasks = []
    for i in range(count_tasks):
        task = asyncio.create_task(delay(delay_sec))
        tasks.append(task)
        # if task.done():
        #     print(f'{task} is done')

    await hello_()
    for i in tasks:
        await i

asyncio.run(main(5, 3))

