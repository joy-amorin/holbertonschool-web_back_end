#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    delay_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time

asyncio.run(wait_random())
