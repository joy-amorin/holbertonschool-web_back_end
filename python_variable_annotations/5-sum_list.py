#!/usr/bin/env python3
"""list of floats"""


def sum_list(input_list: [float]) -> float:
    _sum = 0
    for i in input_list:
        _sum = _sum + i
    return _sum
