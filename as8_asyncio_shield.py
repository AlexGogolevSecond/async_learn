"""asyncio.wait_for asyncio.shield - если указываем таймаут, но не прерываем выполнение задачи"""
import asyncio
from async_learn import delay


async def main():
    delay_task = asyncio.create_task(delay(5))
    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), 3)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Задача заняла более 3 с, скоро она закончится!')
        result = await delay_task
        print(result)

asyncio.run(main())
