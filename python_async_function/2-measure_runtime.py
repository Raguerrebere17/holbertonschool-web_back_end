#!/usr/bin/env python3
"""
Task number 2
"""

from typing import List
import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """Asynchonous coroutine"""
    wait_n: __import__('1-concurrent_coroutines').wait_n
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end= time.time()
    total_time = end - start
    return (total_time / n)
