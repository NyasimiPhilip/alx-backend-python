#!/usr/bin/env python3

import asyncio
import sys
import importlib

sys.path.append("..")  # Add the parent directory to the system path

# Importing the module dynamically
module_name = '0-basic_async_syntax'
module = importlib.import_module(module_name)
wait_random = getattr(module, 'wait_random')

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
hash -r
