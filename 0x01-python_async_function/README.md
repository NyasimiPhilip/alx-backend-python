<h2>Tasks</h2>
    <h3><a href="https://github.com/NyasimiPhilip/alx-backend-python/blob/master/0x01-python_async_function/0-basic_async_syntax.py">0. The basics of async</a></h3>    
    <p>Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.</p>
    <p>Use the random module.</p>
    <pre>        
        <code>
            cat 0-main.py
            #!/usr/bin/env python3
            import asyncio
            wait_random = __import__('0-basic_async_syntax').wait_random
            print(asyncio.run(wait_random()))
            print(asyncio.run(wait_random(5)))
            print(asyncio.run(wait_random(15)))
            ./0-main.py
                9.034261504534394
                1.6216525464615306
                10.634589756751769
        </code>
    </pre>  
    <h3><a href="https://github.com/NyasimiPhilip/alx-backend-python/blob/master/0x01-python_async_function/1-concurrent_coroutines.py">1. Let's execute multiple coroutines at the same time with async</a></h3>    
    <p>Import wait_random from the previous python file that you've written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.</p>
    <p>wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.</p>
    <pre>       
        <code>
            cat 1-main.py
            #!/usr/bin/env python3            '''
            Test file for printing the correct output of the wait_n coroutine            '''
            import asyncio
            wait_n = __import__('1-concurrent_coroutines').wait_n
            print(asyncio.run(wait_n(5, 5)))
            print(asyncio.run(wait_n(10, 7)))
            print(asyncio.run(wait_n(10, 0)))
            ./1-main.py
        </code>
    </pre>  
    <h3><a href="https://github.com/NyasimiPhilip/alx-backend-python/blob/master/0x01-python_async_function/2-measure_runtime.py">2. Measure the runtime</a></h3>   
    <p>From the previous file, import wait_n into 2-measure_runtime.py.</p>
    <p>Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.</p>
    <p>Use the time module to measure an approximate elapsed time.</p>
    <pre>       
        <code>
            cat 2-main.py
            #!/usr/bin/env python3
            measure_time = __import__('2-measure_runtime').measure_time
            n = 5
            max_delay = 9
            print(measure_time(n, max_delay))
        </code>
    </pre>   
    <h3><a href="https://github.com/NyasimiPhilip/alx-backend-python/blob/master/0x01-python_async_function/3-tasks.py">3. Tasks</a></h3>    
    <p>Import wait_random from 0-basic_async_syntax.</p>
    <p>Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task.</p>
    <pre>      
        <code>
            cat 3-main.py
            #!/usr/bin/env python3
            import asyncio
            task_wait_random = __import__('3-tasks').task_wait_random
            async def test(max_delay: int) -&gt; float:
                task = task_wait_random(max_delay)
                await task
                print(task.__class__)
            asyncio.run(test(5))
        </code>
    </pre>   
    <h3><a href="https://github.com/NyasimiPhilip/alx-backend-python/blob/master/0x01-python_async_function/4-tasks.py">4. Tasks</a></h3>   
    <p>Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.</p>
    <pre>       
        <code>
            cat 4-main.py
            #!/usr/bin/env python3
            import asyncio
            task_wait_n = __import__('4-tasks').task_wait_n
            n = 5
            max_delay = 6
            print(asyncio.run(task_wait_n(n, max_delay)))
            ./4-main.py
        </code>
    </pre>   