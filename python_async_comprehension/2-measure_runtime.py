#!/usr/bin/env python3
""" calculates the time it takes to execute 4 coroutines in parallel """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ calculates the time it takes to execute 4 coroutines in parallel """
    start = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end = time.time()
    total_time = end - start
    return total_time
