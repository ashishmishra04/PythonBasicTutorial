# ==========================================================
# VARIABLES
# ==========================================================

# ---------- Basic Data Types ----------
a = 10  # int: integer numeric type (whole number)
b = "Hello"  # str: sequence of Unicode characters (immutable)
c = 3.14  # float: floating-point (decimal) number
d = True  # bool: Boolean (True/False) value
e = [1, 2, 3, 4, 5]  # list: ordered, mutable collection
f = (1, 2, 3)  # tuple: ordered, immutable collection
g = {"name": "John", "age": 30}  # dict: key-value pairs (mutable)
h = {1, 2, 3}  # set: unordered, unique elements
i = None  # NoneType: represents the absence of a value


# ---------- Byte and Binary Types ----------
j = b'Hello'  # bytes: immutable sequence of bytes (binary data)
k = bytearray(b'Hello')  # bytearray: mutable version of bytes

# memoryview: allows direct access to buffer memory (no copying of data)
o = memoryview(b'Hello')

eee = bytes("Hello", 'utf-8')  # converts string to bytes using UTF-8 encoding

# creates mutable byte array (can modify bytes directly)
fff = bytearray(b'Hello')

# gives a view of the bytes object (useful for I/O or large data handling)
jjj = memoryview(b'Hello')


# ---------- Numeric & Math Related ----------
# complex: represents a complex number (real + imaginary part)
l = complex(1, 2)
g = complex(1, 2)  # same as above (example of built-in complex type)
kk = abs(-10)  # abs(): absolute value (removes sign)
ll = round(3.14159, 2)  # round(): rounds to n decimal places
mm = divmod(10, 3)  # divmod(): returns (quotient, remainder)
nn = pow(2, 3)  # pow(): power function (2 ** 3 = 8)
hhh = range(5)  # range: immutable sequence of numbers, often used in loops


# ---------- Advanced / Functional Constructs ----------
# function: callable object that takes input(s) and returns a result
def p(x):
    return x * 2


# generator: produces values lazily (on demand) using iteration
q = (x for x in range(5))
r = type(10)  # type returns the type/class of an object

# iterator: object that returns items one at a time (used in loops)
t = iter([1, 2, 3])

# slice: represents a range for slicing sequences like lists or strings
u = slice(1, 5)

# property: defines getter/setter for class attributes (OOP)
v = property(lambda self: "property")

# w = super()  # super: used in class inheritance to call methods from a parent class


# ---------- Special Constants ----------
# special value indicating that an operation isn’t implemented for given operands
x = NotImplemented

# special constant used as placeholder (e.g., in NumPy or slicing `a[..., 1]`)
y = Ellipsis


# ---------- Modules and Reflection ----------
z = __import__('math')  # dynamically imports a module (like import math)
aa = globals()  # returns a dictionary of current global symbol table (all global variables)
bb = locals()  # returns a dictionary of local variables in the current scope
cc = dir()  # lists names in the current scope (variables, functions, modules, etc.)

# returns a string representation useful for debugging or recreation
dd = repr("Hello")

# evaluates a string as a Python expression (use with caution)
ee = eval("10 + 20")

# executes a string as Python code (no return value)
ff = exec("print('Executed')")

# compiles code into a code object (can later be executed)
gg = compile("print('Compiled')", '<string>', 'exec')


# ---------- Hashing & Object Info ----------
hh = hash("Hello")  # hash(): returns an integer hash (used in sets, dicts)
ii = id(a)  # id(): returns a unique identifier (memory address) for an object
jj = format(10, '04d')  # format(): formats numbers or strings (here -> '0010')


# ---------- Built-in Functions for Logic ----------
# all(): returns True only if all elements are True
oo = all([True, True, False])

# any(): returns True if any element is True
pp = any([True, False, False])


# ---------- Sequence Operations ----------
# sorted(): returns a sorted list (does not modify original)
qq = sorted([3, 1, 2])

# reversed(): returns an iterator reversing sequence order
rr = reversed([1, 2, 3])

# zip(): pairs elements from multiple iterables
ss = zip([1, 2, 3], ['a', 'b', 'c'])

# enumerate(): returns index and value pairs during iteration
tt = enumerate(['a', 'b', 'c'])


# ---------- Functional Tools ----------
uu = map(lambda x: x * 2, [1, 2, 3])  # map(): applies function to each item

# filter(): selects items that meet a condition
vv = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])


# ---------- Type Conversion ----------
ww = list(e)  # converts iterable to list
xx = tuple(e)  # converts iterable to tuple
yy = set(e)  # converts iterable to set
zz = dict(name="Alice", age=25)  # creates dictionary from key-value arguments
aaa = str(123)  # converts to string
bbb = int("123")  # converts string to int
ccc = float("3.14")  # converts string to float
ddd = bool(1)  # converts numeric or string to boolean

# frozenset: immutable version of set (can be used as dict key)
iii = frozenset([1, 2, 3])


# ---------- Exceptions ----------
s = Exception("Error")  # Exception: base class for all exceptions
t = ValueError("Invalid value")  # ValueError: raised for invalid values
u = TypeError("Type mismatch")  # TypeError: raised for type errors
v = KeyError("Missing key")  # KeyError: raised for missing dictionary keys
w = IndexError("Index out of range")  # IndexError: raised for invalid index

# AttributeError: raised for missing attributes
x = AttributeError("No such attribute")

# ImportError: raised for import failures
y = ImportError("Cannot import module")

z = StopIteration()  # StopIteration: signals end of iteration in loops
aa = KeyboardInterrupt()  # KeyboardInterrupt: raised on user interrupt (Ctrl+C)
bb = SystemExit()  # SystemExit: raised to exit the interpreter

# MemoryError: raised when memory is exhausted
cc = MemoryError("Out of memory")

# OverflowError: raised for arithmetic overflow
dd = OverflowError("Numerical overflow")

# ZeroDivisionError: raised for division by zero
ee = ZeroDivisionError("Division by zero")

# FileNotFoundError: raised for missing files
ff = FileNotFoundError("File not found")

gg = IOError("I/O error")  # IOError: raised for I/O operation failures

# RuntimeError: raised for generic runtime errors
hh = RuntimeError("Runtime error")

# ---------------------------------------------------------
