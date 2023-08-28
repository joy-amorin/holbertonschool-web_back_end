#!/usr/bin/env python3
""" string and int/float to tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[str, float]]:
    """takes a string k and an int OR float v as arguments,
    return a tuple, int the first element and the square of v the second """
    return (k, (v * v))
