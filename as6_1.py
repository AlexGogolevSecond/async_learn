"""тут будем отменять задачи"""
import asyncio
from async_learn import delay
from random import randint
from asyncio import CancelledError


async def hello_():
    for i in range(2):
        await asyncio.sleep(1)
        print('pause 1 sec')


async def main(n: int, m: int):
    long_task = asyncio.create_task(delay(10))

    # while True:
    #     is_done = long_task.done()
    #     print(is_done)
    #     print('ждём')
    #     if is_done:
    #         break
    #
    #     await asyncio.sleep(1)

    # seconds_elapsed = 0
    # while not long_task.done():
    #     print(f'Задача не закончилась, след. проверка через секунду. {seconds_elapsed}')
    #     await asyncio.sleep(1)
    #     seconds_elapsed += 1
    #     if seconds_elapsed == 5:
    #         long_task.cancel()
    #         # pass
    #
    # try:
    #     print('before await long_task')
    #     await long_task
    # except CancelledError:
    #     print(f'Задача была снята по истечении {seconds_elapsed} сек.')


asyncio.run(main(randint(1, 7), 3))
