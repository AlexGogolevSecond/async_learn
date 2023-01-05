from asyncio import Future
import asyncio
from datetime import datetime


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    # date_ = f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}'
    # print(f'{date_} before return future')
    return future


async def set_future_value(future) -> None:
    # date_ = f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}'
    # print(f'{date_} before sleep')
    await asyncio.sleep(3)
    future.set_result(42)


async def main():
    future = make_request()
    # date_ = f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}'
    print(f'Будущий объект готов? {future.done()}')
    value = await future
    # date_ = f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}'
    print(f'Будущий объект готов? {future.done()}')
    print(value)

asyncio.run(main())
