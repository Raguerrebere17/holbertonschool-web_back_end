#!/usr/bin/env python3
"""
Task number 1
"""

from typing import List
import asyncio


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Asynchronous coroutine"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
