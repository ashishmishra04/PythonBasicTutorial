# File: intput_data.py
# This script demonstrates various ways to take input from users
# and convert that input into different Python data types.
import ast


# ---------- Safe Evaluation Function ----------
# This function safely evaluates a string expression to a Python literal
# using ast.literal_eval to avoid security risks of eval()
def safe_eval(expr):
    try:
        # Only allow literals using literal_eval
        return ast.literal_eval(expr)
    except (ValueError, SyntaxError):
        return None


try:
    x = input("Enter something: ")
    print("You entered:", x)
except Exception as e:
    print("Error reading input:", e)

# ---------- Type Conversion of Inputs  ----------
try:
    int_input = int(input("Enter an integer: "))
    print("Integer entered:", int_input)
except ValueError:
    print("Error: Please enter a valid integer")

try:
    float_input = float(input("Enter a float: "))
    print("Float entered:", float_input)
except ValueError:
    print("Error: Please enter a valid float number")

try:
    complex_input = complex(input("Enter a complex number (e.g., 1+2j): "))
    print("Complex number entered:", complex_input)
except ValueError:
    print("Error: Please enter a valid complex number")

try:
    list_input = list(
        input("Enter a string to convert to list of characters: "))
    print("List of characters:", list_input)
except Exception as e:
    print("Error creating list:", e)

try:
    tuple_input = tuple(
        input("Enter a string to convert to tuple of characters: "))
    print("Tuple of characters:", tuple_input)
except Exception as e:
    print("Error creating tuple:", e)

try:
    set_input = set(input("Enter a string to convert to set of characters: "))
    print("Set of characters:", set_input)
except Exception as e:
    print("Error creating set:", e)

try:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    dict_input = dict(name=name, age=age)
    print("Dictionary entered:", dict_input)
except ValueError:
    print("Error: Age must be a valid integer")
except Exception as e:
    print("Error creating dictionary:", e)

try:
    str_input = str(input("Enter something to convert to string: "))
    print("String entered:", str_input)
except Exception as e:
    print("Error converting to string:", e)

try:
    bool_input = bool(
        int(input("Enter 0 for False, any other integer for True: ")))
    print("Boolean value:", bool_input)
except ValueError:
    print("Error: Please enter a valid integer (0 or 1)")

# Using safe_eval for complex data structures
print("\nSafe evaluation examples (using ast.literal_eval):")
print("This only allows safe literals like numbers, strings, lists, dicts, etc.")

# Example of using safe_eval for a list
list_str = input("Enter a list (e.g., [1, 2, 3]): ")
eval_list_input = safe_eval(list_str)
if eval_list_input is not None:
    print("Evaluated list:", eval_list_input)
else:
    print("Error: Invalid list format")

# Example of using safe_eval for a dictionary
dict_str = input("Enter a dictionary (e.g., {'key': 'value'}): ")
eval_dict_input = safe_eval(dict_str)
if eval_dict_input is not None:
    print("Evaluated dictionary:", eval_dict_input)
else:
    print("Error: Invalid dictionary format")

# Note: ast.literal_eval is much safer than eval() as it only allows literal expressions
# It prevents execution of arbitrary code that could be harmful
