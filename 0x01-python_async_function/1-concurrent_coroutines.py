#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""


# Importing necessary modules and functions
from typing import List  # Importing List type from the typing module
import asyncio  # Importing the asyncio module
# Importing the wait_random function from another module
wait_random = __import__('0-basic_async_syntax').wait_random


# Defining an asynchronous function named wait_n
async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns the list of all the delays (float values).
    """
    # Creating a list of futures by calling wait_random function n times
    futures = [wait_random(max_delay) for _ in range(n)]
    # Using asyncio.as_completed to iterate over completed futures
    futures = asyncio.as_completed(futures)
    # Awaiting each future and collecting the results (delays) in a list
    delays = [await future for future in futures]
    # Returning the list of delays
    return delays
