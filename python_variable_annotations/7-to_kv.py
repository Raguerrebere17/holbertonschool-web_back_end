#!/usr/bin/env python3
"""
Task 7 - To KV
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to_kv
    """
    return (k, (v * v))
