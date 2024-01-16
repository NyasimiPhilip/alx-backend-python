#!/usr/bin/env python3
"""Creates a generator"""
import asyncio
import random
from typing import Generator


# Define an asynchronous generator function named async_generator
async def async_generator() -> Generator[float, None, None]:
    """Each time asynchronously waits 1 second,
        then yield a random number between 0 and 10"""

    # Loop 10 times
    for _ in range(0, 10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)
        # Yield a random float between 0 and 10
        yield random.uniform(0, 10)
