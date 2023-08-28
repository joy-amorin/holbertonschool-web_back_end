#!/usr/bin/env python3
""" mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ type-annotated function sum_mixed_list which takes a list mxd_lst of
    integers and floats and returns their sum as a float."""

    _sum = 0
    for i in mxd_lst:
        _sum += i
    return float(_sum)
