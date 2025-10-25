# Python internal functions demonstration
print("Demonstrating Python Built-in Functions:\n")
str("Hello, World!")  # Converts to string
int("123")  # Converts to integer
float("123.45")  # Converts to float
len([1, 2, 3, 4, 5])  # Returns length of the list


# functions in Python Def(Define) and Return
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))  # Output: Hello, Alice!


# prefix paramters and suffix parameters in built-in functions
# *args are array of strings [xargs]
def custom_print(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)


custom_print("Hello", "World", sep=', ', end='!\n')  # Output: Hello, World!
# Optional parameters with default values
custom_print("Hello", "World", "Alice")  # Output: Hello World Alice


# xxargs example with dictionary
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_info(name="Bob", age=30, city="New York")
# Output:
# name: Bob
# age: 30
# city: New York
print("\n")


# Lambda Functions
def add(x, y): return x + y


print('add(5, 3): ' + str(add(5, 3)))  # Output: 8
print("\n")


# scope of variables
global_var = "I am global"


def variable_scope_demo():
    local_var = "I am local"
    print(global_var)  # modified global variable
    print(local_var)   # Accessing local variable


variable_scope_demo()  # Output:
# I am global
# I am local
# print(local_var)  # This would raise an error as local_var is not defined globally
print(global_var)  # Output: I am global
