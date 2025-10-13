# ---------- Booleans ----------
bool_true = True
bool_false = False
print('bool_true: ' + str(bool_true))
print('type(bool_true): ' + str(type(bool_true)))
print('bool_false: ' + str(bool_false))
print('type(bool_false): ' + str(type(bool_false)))
print("\n")

# Boolean Operations
a = True
b = False
print('a: ' + str(a) + ', b: ' + str(b))  # Boolean values
print('a and b: ' + str(a and b))  # Logical AND
print('a or b: ' + str(a or b))  # Logical OR
print('not a: ' + str(not a))  # Logical NOT
print('a == b: ' + str(a == b))  # Equality
print('a != b: ' + str(a != b))  # Inequality
print("\n")

# Boolean from other types
print('bool(1): ' + str(bool(1)))  # Non-zero integer to True
print('bool(0): ' + str(bool(0)))  # Zero integer to False
print('bool(-1): ' + str(bool(-1)))  # Non-zero integer to True
print('bool("False"): ' + str(bool("False")))  # Non-empty string to True
print('bool("Hello"): ' + str(bool("Hello")))  # Non-empty string to True
print('bool(""): ' + str(bool("")))  # Empty string to False
print('bool([]): ' + str(bool([])))  # Empty list to False
print('bool([1, 2, 3]): ' + str(bool([1, 2, 3])))  # Non-empty list to True
print("\n")

# ---------- Additional Built-in Functions ----------
# int(): converts boolean to integer (True -> 1, False -> 0)
int_true = int(bool_true)
int_false = int(bool_false)
print('int(True): ' + str(int_true))
print('int(False): ' + str(int_false))
# float(): converts boolean to float (True -> 1.0, False -> 0.0)
float_true = float(bool_true)
float_false = float(bool_false)
print('float(True): ' + str(float_true))
print('float(False): ' + str(float_false))
# str(): converts boolean to string ("True", "False")
str_true = str(bool_true)
str_false = str(bool_false)
print('str(True): ' + str_true)
print('str(False): ' + str_false)
print("\n")

# ---------- None ----------
none_value = None
print('none_value: ' + str(none_value))
print('type(none_value): ' + str(type(none_value)))
print("\n")


# Note: In Python, booleans are a subclass of integers.
