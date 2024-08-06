#!/usr/bin/env python3
"""def"""


wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """block of code"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return (await task for task in asyncio.as_completed(tasks))
