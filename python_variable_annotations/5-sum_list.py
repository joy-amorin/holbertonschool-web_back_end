#!/usr/bin/env python3
from typing import List
"""list of floats"""


def sum_list(input_list: List[float]) -> float:
    """type-annotated function sum_list which takes a list input_list
      of floats as argument and returns their sum as a float."""
    _sum = 0
    for i in input_list:
        _sum = _sum + i
    return _sum
