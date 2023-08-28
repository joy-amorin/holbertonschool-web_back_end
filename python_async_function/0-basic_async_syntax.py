#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay=10):
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
