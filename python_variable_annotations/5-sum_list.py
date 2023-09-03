#!/usr/bin/env python3
"""
Task 5- Sum List
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function Sum_list
    """
    x = 0.0
    for i in input_list:
        x = i + x
    return x
