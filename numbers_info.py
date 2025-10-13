# ---------- Numbers ----------

# Integer
import random
import math
int_value = 10
print('int_value: ' + str(int_value))
print('type(int_value): ' + str(type(int_value)))
print("\n")

# Float
float_value = 3.646459
print('float_value: ' + str(float_value))
print('type(float_value): ' + str(type(float_value)))
# Rounding and Precision and Absolute Value
print('abs(-float_value): ' + str(abs(-float_value)))  # Absolute value
print('round(float_value): ' + str(round(float_value)))  # Rounding
# Rounding to 1 decimal place
print('round(float_value, 1): ' + str(round(float_value, 1)))
# Precision to 2 decimal places (though float_value has only 2 decimal places)
print('format(float_value, ".2f"): ' + format(float_value, '.2f'))
print("\n")

# Complex
complex_value = 1 + 2j
print('complex_value: ' + str(complex_value))
print('type(complex_value): ' + str(type(complex_value)))
print("\n")

# Numeric Operations
a = 10
b = 3
print('a: ' + str(a) + ', b: ' + str(b))  # Numeric values
print('a + b: ' + str(a + b))  # Addition
print('a - b: ' + str(a - b))  # Subtraction
print('a * b: ' + str(a * b))  # Multiplication
print('a / b: ' + str(a / b))  # Division
print('a // b: ' + str(a // b))  # Floor Division
print('a % b: ' + str(a % b))  # Modulus
print('a ** b: ' + str(a ** b))  # Exponentiation
print("\n")


# Type Conversion
int_to_float = float(a)
print('int_to_float: ' + str(int_to_float))
print('type(int_to_float): ' + str(type(int_to_float)))
float_to_int = int(float_value)
print('float_to_int: ' + str(float_to_int))
print('type(float_to_int): ' + str(type(float_to_int)))
complex_to_float = complex_value.real
print('complex_to_float: ' + str(complex_to_float))
print('type(complex_to_float): ' + str(type(complex_to_float)))
print("\n")

# Math Functions
print('math.sqrt(16): ' + str(math.sqrt(16)))  # Square root
print('math.pow(2, 3): ' + str(math.pow(2, 3)))  # Power
print('math.ceil(3.4): ' + str(math.ceil(3.4)))  # Ceiling
print('math.floor(3.7): ' + str(math.floor(3.7)))  # Floor
# Factorial n!=n×(n−1)×(n−2)×⋯×2×1 Example: 5! = 5 × 4 × 3 × 2 × 1
print('math.factorial(5): ' + str(math.factorial(5)))
# GCD Greatest Common Divisor (also called Greatest Common Factor (GCF) or Highest Common Factor (HCF)).
print('math.gcd(12, 15): ' + str(math.gcd(12, 15)))
print("\n")

# Random Number Generation
random_value = random.randint(1, 100)
print('random_value (1-100): ' + str(random_value))
print("\n")

# ---------- End of Numbers ----------
