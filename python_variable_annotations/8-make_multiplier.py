#!/usr/bin/python3
"""
Task 8 - Make Multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its input by the given number
    """
    def multiplier_funct(x: float) -> float:
        return x * multiplier

    return multiplier_funct
