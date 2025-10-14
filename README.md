
# Python Basic Tutorial

Welcome to the **Python Basic Tutorial**! This project demonstrates the fundamental data types, operations, and built-in functions in Python through simple, well-commented code examples. Each file in this repository covers a specific topic. Below is a summary and guide based on the code files:

---

- [Variables and Data Types](#variables-and-data-types-1_variables_infopy)
- [Numbers](#numbers-2_numbers_infopy)
- [Strings](#strings-3_strings_infopy)
- [Booleans and None](#booleans-and-none-4_boolean_infopy)
- [Input and Type Conversion](#input-and-type-conversion-5_intput_datapy)
- [Control Flow](#control-flow-6_control_flowpy)
- [Functions](#functions-7_functionspy)
- [Main Program](#main-program-apppy)

## Variables and Data Types ([`1_variables_info.py`](./1_variables_info.py))
Demonstrates Python's basic and advanced data types:

- **int, float, complex**: Numeric types
- **str**: Text (immutable)
- **bool**: Boolean values
- **list, tuple, set, dict**: Collections
- **bytes, bytearray, memoryview**: Binary data
- **NoneType**: Absence of value
- **range, slice, property, generator, iterator**: Advanced constructs
- **Special constants**: `NotImplemented`, `Ellipsis`, etc.
- **Built-in functions**: `abs`, `round`, `divmod`, `pow`, `repr`, `eval`, `exec`, `compile`, `hash`, `id`, `format`, `all`, `any`, `sorted`, `reversed`, `zip`, `enumerate`, `map`, `filter`, `frozenset`, etc.
- **Exception types**: `Exception`, `ValueError`, `TypeError`, etc.

---

## Numbers ([`2_numbers_info.py`](./2_numbers_info.py))
Shows how to work with numbers in Python:

- **Integer, float, complex** types
- Numeric operations: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Type conversions: `int()`, `float()`, `complex()`
- Math functions: `abs()`, `round()`, `math.sqrt()`, `math.pow()`, `math.ceil()`, `math.floor()`, `math.factorial()`, `math.gcd()`
- Random number generation: `random.randint()`

---

## Strings ([`3_strings_info.py`](./3_strings_info.py))
Explores string operations and methods:

- String creation, length, indexing, and slicing
- Common methods: `upper()`, `lower()`, `replace()`, `split()`, `find()`, `startswith()`, `endswith()`, `strip()`, `count()`, `isalpha()`, `isdigit()`, `isalnum()`
- String formatting: f-strings, `str.format()`, `%` operator
- Escape sequences: `\n`, `\t`, `\\`, `\"`, `\'`, `\r`, `\b`, `\f`, `\uXXXX`, raw strings
- String immutability and joining
- Advanced: `find`, `rfind`, `index`, `rindex`, `in`, `not in`, slicing tricks

---

## Booleans and None ([`4_boolean_info.py`](./4_boolean_info.py))
Demonstrates Boolean logic and the `None` type:

- Boolean values: `True`, `False`
- Logical operations: `and`, `or`, `not`, `==`, `!=`
- Boolean conversion from other types
- Type conversions: `int(True)`, `float(False)`, `str(True)`
- The `None` value and its type
- Note: In Python, `bool` is a subclass of `int`

---

## Input and Type Conversion ([`5_intput_data.py`](./5_intput_data.py))
## Control Flow ([`6_control_flow.py`](./6_control_flow.py))
Demonstrates Python's control flow statements such as if, elif, else, for, while, and break/continue/pass usage.

---
## Functions ([`7_functions.py`](./7_functions.py))
Shows how to define and use functions in Python, including arguments, return values, default parameters, and docstrings.

---
Shows how to take user input and convert it to various types:

- Using `input()` to read strings
- Converting input to `int`, `float`, `complex`, `list`, `tuple`, `set`, `dict`, `str`, `bool`
- Safe evaluation of literals with `ast.literal_eval`
- Error handling for invalid input

---

## Built-in Functions and Advanced Types
See [`variables_info.py`](./variables_info.py) for examples of:

- Reflection: `globals()`, `locals()`, `dir()`
- Dynamic code: `eval()`, `exec()`, `compile()`
- Hashing and object info: `hash()`, `id()`, `format()`
- Sequence operations: `sorted()`, `reversed()`, `zip()`, `enumerate()`
- Functional tools: `map()`, `filter()`
- Type conversion: `list()`, `tuple()`, `set()`, `dict()`, `str()`, `int()`, `float()`, `bool()`, `frozenset()`
- Exception handling: `Exception`, `ValueError`, `TypeError`, etc.

---

## Main Program ([`app.py`](./app.py))
The main script imports all the above modules and prints a welcome message. Each module demonstrates its topic with print statements and examples.

---

## How to Use
Run `app.py` to see the demonstrations. Explore each file for detailed code examples and comments.

---

## References
- [Python Standard Types](https://docs.python.org/3/library/stdtypes.html)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)

---

*This README was generated based on the content of all code files in this project.*
