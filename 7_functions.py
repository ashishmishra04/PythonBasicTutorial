# ==========================================================
# Python internal functions demonstration
# ==========================================================
print("Demonstrating Python Built-in Functions:\n")

str("Hello, World!")       # Converts to string
int("123")                 # Converts to integer
float("123.45")            # Converts to float
len([1, 2, 3, 4, 5])       # Returns length of the list


# ==========================================================
# Functions in Python - Def (Define) and Return
# ==========================================================
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))  # Output: Hello, Alice!


# ==========================================================
# Prefix and Suffix Parameters in Built-in Functions
# ==========================================================
# *args are array-like arguments (variable number of positional args)
def custom_print(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)


custom_print("Hello", "World", sep=', ', end='!\n')   # Output: Hello, World!
# Optional parameters with default values
# Output: Hello World Alice
custom_print("Hello", "World", "Alice")


# ==========================================================
# **kwargs Example (Dictionary-style arguments)
# ==========================================================
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_info(name="Bob", age=30, city="New York")
# Output:
# name: Bob
# age: 30
# city: New York
print("\n")


# ==========================================================
# Lambda Functions
# ==========================================================
def add(x, y): return x + y


print('add(5, 3): ' + str(add(5, 3)))  # Output: 8
print("\n")


# ==========================================================
# Scope of Variables
# ==========================================================
global_var = "I am global"


def variable_scope_demo():
    local_var = "I am local"
    print(global_var)  # Accessing global variable
    print(local_var)   # Accessing local variable


variable_scope_demo()
# Output:
# I am global
# I am local

# print(local_var)  # This would raise an error (local_var not defined globally)
print(global_var)   # Output: I am global

# ==========================================================
