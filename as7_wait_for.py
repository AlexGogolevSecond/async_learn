"""asyncio.wait_for"""
import asyncio
from async_learn import delay


async def main():
    delay_task = asyncio.create_task(delay(5))
    try:
        result = await asyncio.wait_for(delay_task, timeout=2)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? {delay_task.cancelled()}')

asyncio.run(main())

