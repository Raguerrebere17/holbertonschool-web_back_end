#!/usr/bin/env python3
"""
Task number  4
"""

from typing import List
import asyncio
import time
from asyncio import Task


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Asynchronouss coroutine"""
    task_wait_random = __import__('3-tasks').task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
