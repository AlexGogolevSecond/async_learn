import asyncio
from datetime import datetime


async def delay(delay_seconds: int) -> int:
    print(f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}: засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}: сон в течение {delay_seconds} с закончился')
    return delay_seconds
