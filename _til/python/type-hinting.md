---
title: "Using type hints in python (python)"
---
Python is a dynamically typed language. This means it's flexible about the data types that are contained with in variables and objects. Contrast this with a statically typed language like C++ or Java. In statically typed languages, the data type contained within a variable must be declared before the variable can be used. Once the variable is declared and defined, trying to use that variable to store a different type of data will cause a compilation error. In dynamically typed languages like Python, there is no problem changing the data type of a variable.

## Why?

There are some advantages to statically typed languages, and we can take advantage of some of them in Python by using type hints or type annotations, a feature introduced into Python in version 3.6.

First, static typing helps to catch many errors early on in development. In Python, adding type annotations doesn't change the functionality of the code at all. There are external tools like [mypy](http://mypy-lang.org/) or tools built into code editors like Pylance in VSCode that act as "type checkers" and ensure your code is following certain type rules. This can make debugging and testing faster and easier. 

Second, type hints and annotations act as a form of documentation for your code. This can make it easier to read, understand, and maintain.

## Adding type annotations to Python code

Adding useful type hints to python code is as simple as adding a few descriptive annotations to existing function definitions. Consider this example from the [mypy docs](https://mypy.readthedocs.io/en/latest/getting_started.html).

```python
def greeting(name):
    return 'Hello ' + name

def greeting(name: str) -> str:
    return 'Hello ' + name
```

The first function definition is *dynamically typed*. Your type checker has no information regarding the types, and will ignore it. The second version adds the `str` annotation to tell the type checker that the `name` argument and the value returned by the function should both be strings. If you entered `greeting(3)`, your type checker will indicate there is an error because it is receiving an unexpected type.

## The typing module

All of the basic Python data types can be used in type annotations as shown above by typing their own names, for example, `str`, `float`, `bool`. In addition to these, the `typing` module from the standard lib contains many additional objects for typing support.

For example, if you have a function that returns a list, you can use the name of the type: `list`. But this is not enough information. We can go further and indicate the types of the items contained within the list. This works for lists, dicts, sets, tuples, and many other types.

```python
>>> from typing import Dict, List, Tuple

>>> names: List[str] = ["Guido", "Jukka", "Ivan"]
>>> version: Tuple[int, int, int] = (3, 7, 1)
>>> options: Dict[str, bool] = {"centered": False, "capitalize": True}
```

### Union and Optional

If you want to have the option to accept multiple types, for example a function argument that can accept strings or ints, you can use the `Union` type. In the example below, user_id can accept strings or ints.

```python
from typing import Union

def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return 'user-{}'.format(100000 + user_id)
    else:
        return user_id
```

If you want the option for an object to be `None`, you can use `Union[str, None]` or the equivalent, `Optional[str]`.

## More Info
This is just a minimal introduction to the topic and basic functionality, for more info refer to these resources.

[Real Python Type Checking Guide](https://realpython.com/python-type-checking/#functions-without-return-values)

[mypy docs](https://mypy.readthedocs.io/en/latest/introduction.html)

[typing docs](https://docs.python.org/3/library/typing.tml#corresponding-to-collections-in-collections-abc)