  <h1>Python Backend - ALX & Holberton School</h1>
    <h2>Tasks</h2>
    <!-- Task 0 -->
    <h3>0. Basic annotations - add (mandatory)</h3>
    <p>Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.</p>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 0-main.py
        #!/usr/bin/env python3
        add = __import__('0-add').add
        print(add(1.11, 2.22) == 1.11 + 2.22)
        print(add.__annotations__)
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./0-main.py
        True
        {'a':  &lt;class 'float'>, 'b': &lt;class 'float'>, 'return': &lt;class 'float'>}
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 0-add.py</li>
    </ul>
    <!-- Task 1 -->
    <h3>1. Basic annotations - concat (mandatory)</h3>
    <p>Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string.</p>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 1-main.py
        #!/usr/bin/env python3
        concat = __import__('1-concat').concat
        str1 = "egg"
        str2 = "shell"
        print(concat(str1, str2) == "{}{}".format(str1, str2))
        print(concat.__annotations__)
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./1-main.py
        True
        {'str1': &lt;class 'str'>, 'str2': &lt;class 'str'>, 'return': &lt;class 'str'>}
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 1-concat.py</li>
    </ul>
    <!-- Task 2 -->
    <h3>2. Basic annotations - floor (mandatory)</h3>
    <p>Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.</p>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 2-main.py
        #!/usr/bin/env python3
        import math
        floor = __import__('2-floor').floor
        ans = floor(3.14)
        print(ans == math.floor(3.14))
        print(floor.__annotations__)
        print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./2-main.py
        True
        {'n': &lt;class 'float'>, 'return': &lt;class 'int'>}
        floor(3.14) returns 3, which is a &lt;class 'int'>
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 2-floor.py</li>
    </ul>
    <!-- Task 3 -->
    <h3>3. Basic annotations - to string (mandatory)</h3>
    <p>Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.</p>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 3-main.py
        #!/usr/bin/env python3
        to_str = __import__('3-to_str').to_str
        pi_str = to_str(3.14)
        print(pi_str == str(3.14))
        print(to_str.__annotations__)
        print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./3-main.py
        True
        {'n': &lt;class 'float'>, 'return': &lt;class 'str'>}
        to_str(3.14) returns 3.14, which is a &lt;class 'str'>
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 3-to_str.py</li>
    </ul>
    <!-- Task 4 -->
    <h3>4. Define variables (mandatory)</h3>
    <p>Define and annotate the following variables with the specified values:</p>
    <ul>
        <li>a, an integer with a value of 1</li>
        <li>pi, a float with a value of 3.14</li>
        <li>i_understand_annotations, a boolean with a value of True</li>
        <li>school, a string with a value of "Holberton"</li>
    </ul>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 4-main.py
        #!/usr/bin/env python3
        a = __import__('4-define_variables').a
        pi = __import__('4-define_variables').pi
        i_understand_annotations = __import__('4-define_variables').i_understand_annotations
        school = __import__('4-define_variables').school
        print("a is a {} with a value of {}".format(type(a), a))
        print("pi is a {} with a value of {}".format(type(pi), pi))
        print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations),
                                                                            i_understand_annotations))
        print("school is a {} with a value of {}".format(type(school), school))
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./4-main.py
        a is a &lt;class 'int'> with a value of 1
        pi is a &lt;class 'float'> with a value of 3.14
        i_understand_annotations is a &lt;class 'bool'> with a value of True
        school is a &lt;class 'str'> with a value of Holberton
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 4-define_variables.py</li>
    </ul>
    <!-- Task 5 -->
    <h3>5. Complex types - list of floats (mandatory)</h3>
    <p>Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.</p>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 5-main.py
        #!/usr/bin/env python3
        sum_list = __import__('5-sum_list').sum_list
        floats = [3.14, 1.11, 2.22]
        floats_sum = sum_list(floats)
        print(floats_sum == sum(floats))
        print(sum_list.__annotations__)
        print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./5-main.py
        True
        {'input_list': typing.List[float], 'return': &lt;class 'float'>}
        sum_list(floats) returns 6.470000000000001 which is a &lt;class 'float'>
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 5-sum_list.py</li>
    </ul>
    <!-- Task 6 -->
    <h3>6. Complex types - mixed list (mandatory)</h3>
    <p>Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.</p>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 6-main.py
        #!/usr/bin/env python3
        sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list
        print(sum_mixed_list.__annotations__)
        mixed = [5, 4, 3.14, 666, 0.99]
        ans = sum_mixed_list(mixed)
        print(ans == sum(mixed))
        print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./6-main.py
        {'mxd_lst': typing.List[typing.Union[int, float]], 'return': &lt;class 'float'>}
        True
        sum_mixed_list(mixed) returns 679.13 which is a &lt;class 'float'>
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 6-sum_mixed_list.py</li>
    </ul>
    <!-- Task 7 -->
    <h3>7. Complex types - string and int/float to tuple (mandatory)</h3>
    <p>Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.</p>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 7-main.py
        #!/usr/bin/env python3
        to_kv = __import__('7-to_kv').to_kv
        print(to_kv.__annotations__)
        print(to_kv("eggs", 3))
        print(to_kv("school", 0.02))
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./7-main.py
        {'k': &lt;class 'str'>, 'v': typing.Union[int, float], 'return': typing.Tuple[str, float]}
        ('eggs', 9)
        ('school', 0.0004)
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 7-to_kv.py</li>
    </ul>
    <!-- Task 8 -->
    <h3>8. Complex types - functions (mandatory)</h3>
    <p>Write a type-annotated function make_multiplier that takes a float multiplier as an argument and returns a function that multiplies a float by multiplier.</p>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 8-main.py
        #!/usr/bin/env python3
        make_multiplier = __import__('8-make_multiplier').make_multiplier
        print(make_multiplier.__annotations__)
        fun = make_multiplier(2.22)
        print("{}".format(fun(2.22)))
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./8-main.py
        {'multiplier': &lt;class 'float'>, 'return': typing.Callable[[float], float]}
        4.928400000000001
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 8-make_multiplier.py</li>
    </ul>
    <!-- Task 9 -->
    <h3>9. Let's duck type an iterable object (mandatory)</h3>
    <p>Annotate the below function's parameters and return values with the appropriate types:</p>
    <pre>
        def element_length(lst):
            return [(i, len(i)) for i in lst]
    </pre>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 9-main.py
        #!/usr/bin/env python3
        element_length = __import__('9-element_length').element_length
        print(element_length.__annotations__)
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./9-main.py
        {'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 9-element_length.py</li>
    </ul>
    <!-- Task 10 -->
    <h3>10. Duck typing - first element of a sequence (advanced)</h3>
    <p>Augment the following code with the correct duck-typed annotations:</p>
    <pre>
        # The types of the elements of the input are not known
        def safe_first_element(lst):
            if lst:
                return lst[0]
            else:
                return None
    </pre>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 100-main.py
        #!/usr/bin/env python3
        safe_first_element = __import__('100-safe_first_element').safe_first_element
        print(safe_first_element.__annotations__)
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./100-main.py
        {'lst': typing.Sequence[typing.Any], 'return': typing.Union[typing.Any, NoneType]}
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 100-safe_first_element.py</li>
    </ul>
    <!-- Task 11 -->
    <h3>11. More involved type annotations (advanced)</h3>
    <p>Given the parameters and the return values, add type annotations to the function. Hint: look into TypeVar.</p>
    <pre>
        def safely_get_value(dct, key, default=None):
            if key in dct:
                return dct[key]
            else:
                return default
    </pre>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 101-main.py
        #!/usr/bin/env python3
        safely_get_value = __import__('101-safely_get_value').safely_get_value
        annotations = safely_get_value.__annotations__
        print("Here's what the mappings should look like")
        for k, v in annotations.items():
            print("({}: {})".format(k, v))
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./101-main.py
        Here's what the mappings should look like
        (dct: typing.Mapping)
        (key: typing.Any)
        (default: typing.Union[~T, NoneType])
        (return: typing.Union[typing.Any, ~T])
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 101-safely_get_value.py</li>
    </ul>
    <!-- Task 12 -->
    <h3>12. Type Checking (advanced)</h3>
    <p>Use mypy to validate the following piece of code and apply any necessary changes.</p>
    <pre>
        def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
            zoomed_in: Tuple = [
                item for item in lst
                for i in range(factor)
            ]
            return zoomed_in
        array = [12, 72, 91]
        zoom_2x = zoom_array(array)
        zoom_3x = zoom_array(array, 3.0)
    </pre>
    <p><strong>Script:</strong></p>
    <pre>
        bob@dylan:~$ cat 102-main.py
        #!/usr/bin/env python3
        zoom_array = __import__('102-type_checking').zoom_array
        print(zoom_array.__annotations__)
    </pre>
    <p><strong>Execution:</strong></p>
    <pre>
        bob@dylan:~$ ./102-main.py
        {'lst': typing.Tuple, 'factor': &lt;class 'int'>, 'return': typing.List}
    </pre>
    <p><strong>Repo:</strong></p>
    <ul>
        <li>GitHub repository: alx-backend-python</li>
        <li>Directory: 0x00-python_variable_annotations</li>
        <li>File: 102-type_checking.py</li>
    </ul>
