#!/usr/bin/env python3
""" returns a list of tasks """
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ returns a list of tasks """
    float_list: List[float] = []
    for i in range(n):
        float_list.append(await task_wait_random(max_delay))
    return sorted(float_list)
