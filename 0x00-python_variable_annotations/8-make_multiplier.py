#!/usr/bin/env python3
"""def fun"""


from typing import Callable


def make_multiplier(multiplier: float) -> callable[[float], float]:
    """block of code"""
    return lambda x: multiplier * x
