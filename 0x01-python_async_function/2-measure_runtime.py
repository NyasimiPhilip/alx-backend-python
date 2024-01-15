#!/usr/bin/env python3
"""Measures the total execution time for wait_n(n, max_delay)"""

# Importing necessary modules and functions
import asyncio  # Importing the asyncio module
import time  # Importing the time module
# Importing the wait_n function from another module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns total_time (total execution time) / n"""

    # Recording the start time using time.perf_counter()
    start_time = time.perf_counter()
    # Running the wait_n function asynchronously using asyncio.run
    asyncio.run(wait_n(n, max_delay))
    # Recording the end time using time.perf_counter()
    end_time = time.perf_counter()
    # Calculating the total execution time and dividing by n to get the average
    return (end_time - start_time) / n
