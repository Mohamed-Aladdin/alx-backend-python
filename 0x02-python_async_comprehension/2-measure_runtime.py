#!/usr/bin/env python3
"""Task 2 Module"""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Import async_comprehension from the previous file and
    write a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    """

    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
