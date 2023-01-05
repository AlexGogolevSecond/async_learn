import asyncio
from async_learn import async_timed, delay, get_fib


@async_timed
async def main():
    await asyncio.create_task(get_fib(10))

asyncio.run(main())

