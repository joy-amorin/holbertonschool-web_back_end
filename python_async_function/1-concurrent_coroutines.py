#!/usr/bin/env python3
"""execute multiple coroutines at the
 same time with async"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay."""

    list_delay = []

    for _ in range(n):
        list_delay.append(wait_random(max_delay))
    # umpacking operator "*" to pass all list_delay elements as arguments
    results = await asyncio.gather(*list_delay)

    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if results[j] < results[min]:
                min = j
        results[i], results[min] = results[min], results[i]
    return results
