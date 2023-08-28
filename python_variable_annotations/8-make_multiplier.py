#!/usr/bin/env python3
"""functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ takes a float multiplier as argument and returns a
      function that multiplies a float by multiplier."""

    def multiplies(f: float) -> float:
        return f * multiplier
    return multiplies
