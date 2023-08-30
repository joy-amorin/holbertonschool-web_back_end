#!/usr/bin/env python3
""" Measure the runtime """
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the total execution time """
    t1 = time.time()
    asyncio.run(wait_n(n, max_delay))
    t2 = time.time()
    total_time = t2 - t1
    return total_time / n
