#!/usr/bin/env python3
"""Defines an asynchronous coroutine"""

# Importing necessary modules
import asyncio
import random


# Defining an asynchronous coroutine named wait_random
async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay.

    Args:
        max_delay (int): The maximum delay time (default is 10).

    Returns:
        float: The random delay time.
    """
    # Generate a random number within the specified range
    random_number = random.uniform(0, max_delay)

    # Asynchronously sleep for the generated random time
    await asyncio.sleep(random_number)

    # Return the generated random delay time
    return random_number
