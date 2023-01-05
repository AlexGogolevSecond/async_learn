import asyncio
from async_learn import async_timed


@async_timed
async def delay(delay_sec: int) -> int:
    print(f'засыпаю на {delay_sec} c.')
    await asyncio.sleep(delay_sec)
    print(f'сон в течение {delay_sec} c. закончился')
    return delay_sec


@async_timed
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two

asyncio.run(main())


