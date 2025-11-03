# ==============================================================
# Demonstrating Python Data Structures
# ==============================================================

from sys import getsizeof
import array
from collections import deque
print("Demonstrating Python Data Structures:\n")
# Demonstrating Python Data Structures:


######################################################
# list
######################################################
my_list = [1, 3, 5, 7, 8]
print('my_list: ' + str(my_list))
# my_list: [1, 3, 5, 7, 8]

print('type(my_list): ' + str(type(my_list)))
# type(my_list): <class 'list'>

print('my_list[0]: ' + str(my_list[0]))  # Accessing first element
# my_list[0]: 1

my_list.append(6)  # Adding an element
print('my_list after append(6): ' + str(my_list))
# my_list after append(6): [1, 3, 5, 7, 8, 6]

my_list.remove(3)  # Removing an element
print('my_list after remove(3): ' + str(my_list))
# my_list after remove(3): [1, 5, 7, 8, 6]

my_list.sort()
print('my_list after sort(): ' + str(my_list))
# my_list after sort(): [1, 5, 6, 7, 8]
print("\n")


######################################################
# tuple
# ###### Tuples are immutable, so we cannot add or remove elements ####
######################################################
my_tuple = (1, 2, 3, 4, 5)
my_tuple = tuple([1, 2, 3, 4, 5])  # alternative way to create tuple
my_tuple = 1, 2, 3, 4, 5  # another way to create tuple without parentheses
print('my_tuple: ' + str(my_tuple))
# my_tuple: (1, 2, 3, 4, 5)

print('type(my_tuple): ' + str(type(my_tuple)))
# type(my_tuple): <class 'tuple'>

print('my_tuple[0]: ' + str(my_tuple[0]))  # Accessing first element
# my_tuple[0]: 1
print("\n")

# list vs tuple
print('List is mutable, Tuple is immutable.')
# List is mutable, Tuple is immutable.
print("\n")


######################################################
# set
######################################################
my_set = {1, 2, 3, 4, 5}
print('my_set: ' + str(my_set))
# my_set: {1, 2, 3, 4, 5}

print('type(my_set): ' + str(type(my_set)))
# type(my_set): <class 'set'>

my_set.add(6)  # Adding an element
print('my_set after add(6): ' + str(my_set))
# my_set after add(6): {1, 2, 3, 4, 5, 6}

my_set.remove(3)  # Removing an element
print('my_set after remove(3): ' + str(my_set))
# my_set after remove(3): {1, 2, 4, 5, 6}
print("\n")

######################################################
#  set operations Other features like [union, intersection, difference, symmetric difference]
#  set don't allow duplicate values and don't support indexing
######################################################
numbers = [1, 1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)  # Removing duplicates
print('unique_numbers from list: ' + str(unique_numbers))
# unique_numbers from list: {1, 2, 3, 4, 5}

# set operations: union |, intersection &, difference -, symmetric difference ^
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# UNION
union_set = set_a.union(set_b)
# or
union_set = set_a | set_b
print('Union of set_a and set_b: ' + str(union_set))
# Union of set_a and set_b: {1, 2, 3, 4, 5}

# INTERSECTION
intersection_set = set_a.intersection(set_b)
# or
intersection_set = set_a & set_b
print('Intersection of set_a and set_b: ' + str(intersection_set))
# Intersection of set_a and set_b: {3}

# DIFFERENCE
difference_set = set_a.difference(set_b)
# or
difference_set = set_a - set_b
print('Difference of set_a and set_b: ' + str(difference_set))
# Difference of set_a and set_b: {1, 2}

# SYMMETRIC DIFFERENCE
symmetric_difference_set = set_a.symmetric_difference(set_b)
# or
symmetric_difference_set = set_a ^ set_b
print('Symmetric Difference of set_a and set_b: ' + str(symmetric_difference_set))
# Symmetric Difference of set_a and set_b: {1, 2, 4, 5}
print("\n")


######################################################
# dictionary
######################################################
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print('my_dict: ' + str(my_dict))
# my_dict: {'name': 'Alice', 'age': 30, 'city': 'New York'}

print('type(my_dict): ' + str(type(my_dict)))
# type(my_dict): <class 'dict'>

print("my_dict['name']: " + my_dict['name'])  # Accessing value by key
# my_dict['name']: Alice

my_dict['age'] = 31  # Modifying a value
print("my_dict after modifying age: " + str(my_dict))
# my_dict after modifying age: {'name': 'Alice', 'age': 31, 'city': 'New York'}

my_dict['country'] = 'USA'  # Adding a new key-value pair
print("my_dict after adding country: " + str(my_dict))
# my_dict after adding country: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}
print("\n")

######################################################
# dictionary fuction dict
# ######################################################
point = dict(x=10, y=20)
print('point dictionary using dict(): ' + str(point))
# point dictionary using dict(): {'x': 10, 'y': 20}

# comprehensive way to create dictionary
squares_dict = {x: x ** 2 for x in range(6)}
print('squares_dict using comprehension: ' + str(squares_dict))
# squares_dict using comprehension: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("\n")


######################################################
# Combining Data Structures
######################################################
letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3] * 3  # Repeating list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 2D list
combine = letters + numbers  # Combining lists

print('letters: ' + str(letters))
# letters: ['a', 'b', 'c', 'd', 'e']

print('numbers: ' + str(numbers))
# numbers: [1, 2, 3, 1, 2, 3, 1, 2, 3]

print('matrix: ' + str(matrix))
# matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('combine = letters + numbers: ' + str(combine))
# combine = letters + numbers: ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 1, 2, 3, 1, 2, 3]

combine = letters + numbers + matrix
print('combine = [letters + numbers + matrix]: ' + str(combine))
# combine = [letters + numbers + matrix]: ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 1, 2, 3, 1, 2, 3, [1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\n")


######################################################
# List range (starts, stops, step)
######################################################
range_list = list(range(1, 11))  # List of numbers from 1 to 10
print('range_list (1 to 10): ' + str(range_list))
# range_list (1 to 10): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

range_list = list(range(0, 21, 2))  # List of even numbers from 0 to 20
print('range_list (even numbers 0 to 20): ' + str(range_list))
# range_list (even numbers 0 to 20): [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print("\n")


######################################################
# list unpacking
######################################################
a, b, c, d, e = letters = ['a', 'b', 'c', 'd', 'e']
print('Unpacked letters: ' + a + ', ' + b + ', ' + c + ', ' + d + ', ' + e)
# Unpacked letters: a, b, c, d, e

first, *middle, last = numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Unpacked numbers: first=' + str(first) +
      ', middle=' + str(middle) + ', last=' + str(last))
# Unpacked numbers: first=1, middle=[2, 3, 4, 5, 6, 7, 8], last=9

unpacked_values = [*letters]  # values after * must be in a list or tuple
print('Unpacked values using * : ' + str(unpacked_values))
# Unpacked values using * : ['a', 'b', 'c', 'd', 'e']
print("\n")


######################################################
# loop through list
######################################################
for item in my_list:
    print('List item: ' + str(item))
print("\n")

# loop through enumerate list
for index, item in enumerate(my_list):
    print('List item at index ' + str(index) + ': ' + str(item))
print("\n")

# loop through dictionary
for key, value in my_dict.items():
    print('Dictionary key: ' + str(key) + ', value: ' + str(value))
print("\n")


#########################################################
# Add/Remove Items to Data Structures
#########################################################
letters = ['a', 'b', 'c', 'd', 'e']

letters.append('f')  # Adding to list
print('letters after append(\'f\'): ' + str(letters))
# letters after append('f'): ['a', 'b', 'c', 'd', 'e', 'f']

letters.insert(0, 'z')  # Inserting at the beginning
print('letters after insert(0, \'z\'): ' + str(letters))
# letters after insert(0, 'z'): ['z', 'a', 'b', 'c', 'd', 'e', 'f']

letters.pop()  # Removing last element
print('letters after pop(): ' + str(letters))
# letters after pop(): ['z', 'a', 'b', 'c', 'd', 'e']

letters.remove('c')  # Removing specific element
print('letters after remove(\'c\'): ' + str(letters))
# letters after remove('c'): ['z', 'a', 'b', 'd', 'e']

letters.extend(['g', 'h'])  # Extending list
print('letters after extend([\'g\', \'h\']): ' + str(letters))
# letters after extend(['g', 'h']): ['z', 'a', 'b', 'd', 'e', 'g', 'h']

del letters[0]  # Deleting first element
print('letters after del letters[0]: ' + str(letters))
# letters after del letters[0]: ['a', 'b', 'd', 'e', 'g', 'h']

del letters[1:3]  # Deleting a slice
# this will delete 'b' and 'd' index 1 and 2
print('letters after del letters[1:3]: ' + str(letters))
# letters after del letters[1:3]: ['a', 'e', 'g', 'h']

letters.clear()  # Clearing the list
print('letters after clear(): ' + str(letters))
# letters after clear(): []
print("\n")

#########################################################
# find items in list
#########################################################
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print("'c' in letters: " + str('c' in letters))
# 'c' in letters: True

print("'z' not in letters: " + str('z' not in letters))
# 'z' not in letters: True

print("letters.index('d'): " + str(letters.index('d')))
# letters.index('d'): 3

print("letters.count('a'): " + str(letters.count('a')))
# letters.count('a'): 1
print("\n")


#########################################################
# sort and reverse
#########################################################
numbers = [5, 2, 9, 1, 5, 6]

numbers.sort()  # Ascending
print('numbers after sort(): ' + str(numbers))
# numbers after sort(): [1, 2, 5, 5, 6, 9]

numbers.sort(reverse=True)  # Descending
print('numbers after sort(reverse=True): ' + str(numbers))
# numbers after sort(reverse=True): [9, 6, 5, 5, 2, 1]

numbers.reverse()  # Reversing order
print('numbers after reverse(): ' + str(numbers))
# numbers after reverse(): [1, 2, 5, 5, 6, 9]
print("\n")


#########################################################
# copy list
#########################################################
original = [1, 2, 3, 4]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

print('original: ' + str(original))
# original: [1, 2, 3, 4]
print('copy1: ' + str(copy1))
# copy1: [1, 2, 3, 4]
print('copy2: ' + str(copy2))
# copy2: [1, 2, 3, 4]
print('copy3: ' + str(copy3))
# copy3: [1, 2, 3, 4]
print("\n")


#########################################################
# nested lists
#########################################################
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print('matrix: ' + str(matrix))
# matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('matrix[0][0]: ' + str(matrix[0][0]))
# matrix[0][0]: 1
print('matrix[1][2]: ' + str(matrix[1][2]))
# matrix[1][2]: 6
print("\n")

# loop through matrix
for row in matrix:
    for col in row:
        print(col, end=' ')
    print()
# Output:
# 1 2 3
# 4 5 6
# 7 8 9
print("\n")


#########################################################
# list comprehension
# [expression for item in iterable if condition]
#########################################################
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [n ** 2 for n in numbers]
print('squares: ' + str(squares))
# squares: [1, 4, 9, 16, 25, 36, 49, 64, 81]

even = [n for n in numbers if n % 2 == 0]
print('even: ' + str(even))
# even: [2, 4, 6, 8]

odd_squares = [n ** 2 for n in numbers if n % 2 != 0]
print('odd_squares: ' + str(odd_squares))
# odd_squares: [1, 9, 25, 49, 81]

# Nested list comprehension example
matrix_2d = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix_2d for num in row]
print('flattened: ' + str(flattened))
# flattened: [1, 2, 3, 4, 5, 6]
print("\n")


#########################################################
# zip and unpack
#########################################################
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

combined = list(zip(names, ages))
print('combined: ' + str(combined))
# combined: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

unzipped_names, unzipped_ages = zip(*combined)
print('unzipped_names: ' + str(unzipped_names))
# unzipped_names: ('Alice', 'Bob', 'Charlie')
print('unzipped_ages: ' + str(unzipped_ages))
# unzipped_ages: (25, 30, 35)
print("\n")


#########################################################
# dictionary comprehensions
#########################################################
squares_dict = {x: x ** 2 for x in range(6)}
print('squares_dict: ' + str(squares_dict))
# squares_dict: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even_dict = {x: x ** 2 for x in range(10) if x % 2 == 0}
print('even_dict: ' + str(even_dict))
# even_dict: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
print("\n")


#########################################################
# set comprehensions
#########################################################
unique_squares = {x ** 2 for x in [1, 2, 2, 3, 3, 4]}
print('unique_squares: ' + str(unique_squares))
# unique_squares: {16, 1, 4, 9}
print("\n")


#########################################################
# tuple unpacking in loops
#########################################################
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for number, letter in pairs:
    print(f'Number: {number}, Letter: {letter}')
# Number: 1, Letter: a
# Number: 2, Letter: b
# Number: 3, Letter: c
print("\n")


#########################################################
# nested dictionary and list access
#########################################################
data = {
    'person': {
        'name': 'John',
        'age': 40,
        'hobbies': ['reading', 'cycling', 'traveling']
    }
}

print("data['person']['name']: " + data['person']['name'])
# data['person']['name']: John
print("data['person']['hobbies'][1]: " + data['person']['hobbies'][1])
# data['person']['hobbies'][1]: cycling
print("\n")


#########################################################
# Using enumerate, zip, and comprehension together
#########################################################
names = ['Anna', 'Brian', 'Cathy']
scores = [85, 90, 88]

result = {name: score for i, (name, score) in enumerate(zip(names, scores))}
print('result: ' + str(result))
# result: {'Anna': 85, 'Brian': 90, 'Cathy': 88}
print("\n")


#########################################################
# filter, map, and lambda
#########################################################
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print('even_numbers: ' + str(even_numbers))
# even_numbers: [2, 4, 6]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print('squared_numbers: ' + str(squared_numbers))
# squared_numbers: [1, 4, 9, 16, 25, 36]

sum_of_numbers = sum(numbers)
print('sum_of_numbers: ' + str(sum_of_numbers))
# sum_of_numbers: 21
print("\n")

#########################################################
# Stacks [LIFO] and Queues [FIFO] using lists
#########################################################

stack = []  # Using list as stack
stack.append(1)
stack.append(2)
stack.append(3)
print('stack after pushes: ' + str(stack))
# stack after pushes: [1, 2, 3]

stack.pop()  # Popping last element
print('stack after pop: ' + str(stack))
# stack after pop: [1, 2]
print("\n")

queue = []  # Using list as queue
queue.append(1)
queue.append(2)
queue.append(3)
print('queue after enqueues: ' + str(queue))
# queue after enqueues: [1, 2, 3]
queue.pop(0)  # Dequeuing first element
print('queue after dequeue: ' + str(queue))
# queue after dequeue: [2, 3]

# deque from collections for efficient queue
efficient_queue = deque()
efficient_queue.append(1)
efficient_queue.append(2)
efficient_queue.append(3)
print('efficient_queue after enqueues: ' + str(efficient_queue))
# efficient_queue after enqueues: deque([1, 2, 3])
efficient_queue.popleft()  # Dequeuing first element
print('efficient_queue after dequeue: ' + str(efficient_queue))
# efficient_queue after dequeue: deque([2, 3])
print("\n")

#########################################################
# Swapping values in a list [underneeth its creating tuple and unpacking it]
#########################################################
values = [10, 20]
print('Original values: ' + str(values))
# Original values: [10, 20]
values[0], values[1] = values[1], values[0]
print('Swapped values: ' + str(values))
print("\n")


#########################################################
# Array module for large data and data is type specific
#########################################################
large_array = array.array('i', range(1000))  # 'i' for signed integers
print('First 10 elements of large_array: ' + str(large_array[:10]))
# First 10 elements of large_array: array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("\n")

#########################################################
# Generators for memory efficient data handling
# you can generate values on the fly with no indexing and no storing all values in memory
#########################################################
values = (x*2 for x in range(1000000))  # Generator expression
print('Size of generator object: ' + str(getsizeof(values)) + ' bytes')
# Size of generator object: 208 bytes
values = [x*2 for x in range(1000000)]  # List comprehension for comparison
print('size of list generator object: ' + str(getsizeof(values)) + ' bytes')
# size of list generator object: 8448728 bytes
print("\n")


#########################################################
# Conclusion
#########################################################
print("✅ Demonstration of Python data structures completed successfully!")
# ✅ Demonstration of Python data structures completed successfully!
