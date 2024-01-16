#!/usr/bin/env python3
"""Measures time"""
import asyncio
import time

# Import the async_comprehension from the previous module
async_comprehension = __import__('1-async_comprehension').async_comprehension


# Define an asynchronous function named measure_runtime
async def measure_runtime() -> float:
    """Executes async_comprehension four times in parallel
        and measure_runtime should measure the total runtime and return it"""
    # Record the start time using time.perf_counter()
    start_time = time.perf_counter()

    # Use asyncio.gather to run async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    # Calculate the total runtime by
    # subtracting the start time from the current time
    return time.perf_counter() - start_time
