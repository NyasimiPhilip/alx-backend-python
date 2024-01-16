#!/usr/bin/env python3
"""Generates a list from an async comprehension"""
from typing import List

# Import the async_generator from the previous module
async_generator = __import__('0-async_generator').async_generator


# Define an asynchronous function named async_comprehension
async def async_comprehension() -> List[float]:
    """Collects async generated list and return it"""
    # Use an async comprehension to iterate
    # over the values from async_generator
    # The loop variable (_) is not used in the comprehension
    # The result is a list of float values
    return [_ async for _ in async_generator()]
