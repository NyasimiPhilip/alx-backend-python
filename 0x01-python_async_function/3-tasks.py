#!/usr/bin/env python3
"""Create a task"""
import asyncio
from typing import Any

# Importing the wait_random function from another module
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return a task for the wait_random coroutine with the max_delay."""
    # Creating and returning a task using asyncio.create_task
    return asyncio.create_task(wait_random(max_delay))
