#!/usr/bin/env python3
"""
Task number 3
"""

from typing import List
import time
import asyncio
from asyncio import Task


def task_wait_random(max_delay: int) -> Task:
    """Asynchronous coroutine"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
