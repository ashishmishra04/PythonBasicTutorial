# Length of a string
string_value = "Hello World! 123"
print('string_value: ' + string_value)
print('len(string_value): ' + str(len(string_value)))
print("\n")

# ---------- String Operations ----------
# Convert to uppercase (no parameters)
print('upper() : ' + string_value.upper())
# Convert to lowercase (no parameters)
print('lower() : ' + string_value.lower())
# Replace substring ("World", "Python")
print('replace("World", "Python") : ' +
      string_value.replace("World", "Python"))
# Split into a list of words (default: splits by whitespace)
print('split() : ' + str(string_value.split()))
# Find substring index ("World")
print('find("World") : ' + str(string_value.find("World")))
# Check if starts with substring ("Hello")
print('startswith("Hello") : ' + str(string_value.startswith("Hello")))
# Check if ends with substring ("!")
print('endswith("!") : ' + str(string_value.endswith("!")))
# Remove leading/trailing characters ("!")
print('strip("3") : ' + string_value.strip("3"))
# Count occurrences of a substring ("o")
print('count("o") : ' + str(string_value.count("o")))
# Check if all characters are alphabetic (no parameters)
print('isalpha() : ' + str(string_value.isalpha()))
# Check if all characters are digits (no parameters)
print('isdigit() : ' + str(string_value.isdigit()))
# Check if all characters are alphanumeric (no parameters)
print('isalnum() : ' + str(string_value.isalnum()))

print("\n")
# String Operations
course = "Python Programming"
print('course: ' + course)
print('len(course): ' + str(len(course)))  # Length
print('course[0]: ' + course[0])    # first character
print('course[-1]: ' + course[-1])  # last character
print('course[0:6]' + course[0:6])  # Slicing
print('course[7:]' + course[7:])    # Slicing from index 7 to end
print('course[:6]' + course[:6])    # Slicing from start to index 6
print('course[:]' + course[:])      # Full string
print('course[-11:-1]' + course[-11:-1])  # Slicing with negative indices
print('course[::2]' + course[::2])  # Slicing with step

print("\n")
# Escape Sequences
# Double quotes inside double quotes
print('with double quotes: ' + "He said, \"Hello!\"")
# Single quote inside single quotes
print('with single quotes: ' + 'It\'s a sunny day.')
# Backslash character
print('with \ quotes: ' + "Men \\ Women \\ Kids")
# Newline character
print('with newline: ' + "Hello\nWorld")
# Tab character
print('with tab: ' + "Hello\tWorld")
# Carriage return
print('with carriage return: ' + "Hello\rWorld")
# Backspace character
print('with backspace: ' + "Hello\bWorld")
# Formfeed character
print('with formfeed: ' + "Hello\fWorld")
# Unicode character (e.g., smiley face)
print('with unicode: ' + "Hello\u263A")  # ☺
# Raw string (ignores escape sequences)
print(r'with raw string: ' + r"C:\Users\Name\Documents")
print("\n")

# ---------- String Formatting ----------
name = "Alice"
age = 30
height = 5.7
# Using f-strings (Python 3.6+)
print(f'Name: {name}, Age: {age}, Height: {height}')
# Using str.format()
print('Name: {}, Age: {}, Height: {}'.format(name, age, height))
# Using % operator
print('Name: %s, Age: %d, Height: %.1f' % (name, age, height))
print("\n")
# ---------- Escape Sequences Summary ----------
print(r'\n : Newline')
print(r'\t : Tab')
print(r'\\ : Backslash')
print(r'\" : Double Quote')
print(r"\' : Single Quote")
print(r'\r : Carriage Return')
print(r'\b : Backspace')
print(r'\f : Formfeed')
print(r'\uXXXX : Unicode Character')
print(r'r"string" : Raw String (ignores escape sequences)')
print("\n")

# ---------- Common String Methods Summary ----------
print('upper() : Converts to uppercase')
print('lower() : Converts to lowercase')
print('title() : Converts to title case')  # Each word capitalized
print('capitalize() : Capitalizes first character')
print('replace(old, new) : Replaces substring')
print('split() : Splits into a list of words')
print('find(sub) : Finds substring index')
print('startswith(sub) : Checks if starts with substring')
print('endswith(sub) : Checks if ends with substring')
print('strip(chars) : Removes leading/trailing characters')
print('count(sub) : Counts occurrences of substring')
print('isalpha() : Checks if all characters are alphabetic')
print('isdigit() : Checks if all characters are digits')
print('isalnum() : Checks if all characters are alphanumeric')
print("\n")

# ---------- String Immutability ----------
original = "Hello"
modified = original.replace("H", "J")
print('original: ' + original)  # Original string remains unchanged
print('modified: ' + modified)  # New string with modification
print("\n")

# ---------- String stripping ----------
s = "   Hello World!   "
print('Original: "' + s + '"')
# Removes leading/trailing whitespace
print('strip(): "' + s.strip() + '"')
print('lstrip(): "' + s.lstrip() + '"')        # Removes leading whitespace
print('rstrip(): "' + s.rstrip() + '"')        # Removes trailing whitespace
print('strip(" H!"): "' + s.strip(" H!") + '"')  # Removes specified characters
print("\n")

# ---------- String Joining ----------
words = ["Hello", "World", "from", "Python"]
print('Words list: ' + str(words))
print('Join with space: ' + ' '.join(words))        # Join with space
print('Join with comma: ' + ', '.join(words))       # Join with comma
print('Join with hyphen: ' + '-'.join(words))       # Join with hyphen
print('Join with no separator: ' + ''.join(words))   # Join with no separator
print("\n")

# ---------- String Formatting Methods ----------
value = 42
print('Using f-string: ' + f'Value is {value}')               # f-string
print('Using str.format(): ' + 'Value is {}'.format(value))    # str.format
print('Using % operator: ' + 'Value is %d' % value)            # % operator
print("\n")

# ---------- String find  ----------
text = "The quick brown fox jumps over the lazy dog. The dog barked."
print('Text: ' + text)
print('find("dog"): ' + str(text.find("dog")))          # First occurrence
print('rfind("dog"): ' + str(text.rfind("dog")))        # Last occurrence
# First occurrence (raises error if not found)
print('index("dog"): ' + str(text.index("dog")))
# Last occurrence (raises error if not found)
print('rindex("dog"): ' + str(text.rindex("dog")))
print('in operator: ' + str("dog" in text))  # Check if substring exists
# Check if substring does not exist
print('not in operator: ' + str("cat" not in text))
print("\n")

# ---------- Trick Questions ----------
fruit = "Apple"
print('fruit: ' + fruit)
# string[start:end]
# start → the index to begin from (inclusive)
# end → the index to stop before(exclusive)
# fruit[1:-1]
# means:
# start at index 1 → 'p'
# Stop before index - 1 → 'e' (not included)
# 👉 Therefore, it includes indices 1, 2, 3 → "ppl"
print('fruit[1:-1]: ' + fruit[1:-1])      # Last character
