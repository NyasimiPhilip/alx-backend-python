<section>
    <h2>0. Async Generator<br><code><a href="https://github.com/NyasimiPhilip/alx-backend-python/blob/master/0x02-python_async_comprehension/0-async_generator.py">0-async_generator.py</a></code></h2>
    <p>Write a coroutine called <code>async_generator</code> that takes no arguments.</p>
    <p>The coroutine will loop 10 times, each time asynchronously waiting 1 second, then yielding a random number between 0 and 10. Use the random module.</p>
    <pre><code>
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values());
    </code></pre>
    <p>Output:</p>
    <pre><code>
[4.403136952967102,<br>
 6.9092712604587465,<br>
  6.293445466782645,<br> 
  4.549663490048418,<br>
  4.1326571686139015,<br>
  9.99058525304903,<br>
  6.726734105473811,<br>
  9.84331704602206,<br>
  1.0067279479988345,<br>
  1.3783306401737838]
    </code></pre>
    
</section>

<section>
    <h2>1. Async Comprehensions <br><code><a href="https://github.com/NyasimiPhilip/alx-backend-python/blob/master/0x02-python_async_comprehension/1-async_comprehension.py"></h2>
    <p>Import <code>async_generator</code> from the previous task and then write a coroutine called <code>async_comprehension</code> that takes no arguments.</p>
    <p>The coroutine will collect 10 random numbers using an async comprehension over <code>async_generator</code>, then return the 10 random numbers.</p>
    <pre><code>
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main());
    </code></pre>
    <p>Output:</p>
    <pre><code>
[9.861842105071727,<br>
8.572355293354995,<br>
1.7467182056248265,<br>
4.0724372912858575,<br>
0.5524750922145316,<br>
8.084266576021555,<br>
8.387128918690468,<br>
1.5486451376520916,<br>
7.713335177885325,<br>
7.673533267041574]
    </code></pre>   
</section>

<section>
    <h2>2. Run time for four parallel comprehensions<br><code><a href="https://github.com/NyasimiPhilip/alx-backend-python/blob/master/0x02-python_async_comprehension/2-measure_runtime.py">2-measure_runtime.py</a> </h2>
    <p>Import <code>async_comprehension</code> from the previous file and write a <code>measure_runtime</code> coroutine that will execute <code>async_comprehension</code> four times in parallel using <code>asyncio.gather</code>.</p>
    <p><code>measure_runtime</code> should measure the total runtime and return it.</p>
    <p>Notice that the total runtime is roughly 10 seconds, explain it to yourself.</p>
    <pre><code>
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await measure_runtime()

print(
    asyncio.run(main())
);
    </code></pre>
    <p>Output:</p>
    <pre><code>
10.021936893463135
    </code></pre> 
</section>
