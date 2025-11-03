# Data Structures in Python
print("Demonstrating Python Data Structures:\n")
# Demonstrating Python Data Structures:

######################################################
# list
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
# tuple ###### Tuples are immutable, so we cannot add or remove elements ####
my_tuple = (1, 2, 3, 4, 5)
print('my_tuple: ' + str(my_tuple))
# my_tuple: (1, 2, 3, 4, 5)
print('type(my_tuple): ' + str(type(my_tuple)))
# type(my_tuple): <class 'tuple'>
print('my_tuple[0]: ' + str(my_tuple[0]))  # Accessing first element
# my_tuple[0]: 1
#
print("\n")

# list vs tuple
print('List is mutable, Tuple is immutable.')
# List is mutable, Tuple is immutable.
print("\n")

######################################################
# set
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
# dictionary
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
# Combining Data Structures
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

###############################################
# List range (starts, stops, step)
range_list = list(range(1, 11))  # List of numbers from 1 to 10
print('range_list (1 to 10): ' + str(range_list))
# range_list (1 to 10): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

range_list = list(range(0, 21, 2))  # List of even numbers from 0 to 20
print('range_list (even numbers 0 to 20): ' + str(range_list))
# range_list (even numbers 0 to 20): [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

####################################################
# list unpacking
a, b, c, d, e = letters = ['a', 'b', 'c', 'd', 'e']
print('Unpacked letters: ' + a + ', ' + b + ', ' + c + ', ' + d + ', ' + e)
# Unpacked letters: a, b, c, d, e
first, *middle, last = numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Unpacked numbers: first=' + str(first) +
      ', middle=' + str(middle) + ', last=' + str(last))
# Unpacked numbers: first=1, middle=[2, 3, 4, 5, 6, 7, 8], last=9
print("\n")

#####################################################
# loop through list
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
# find items in Data Structures
letters = ['a', 'b', 'c', 'd', 'e']
print('letters: ' + str(letters))
# find item in Data Structures
print('find a item exits \'d\' in letters: False' + 'd' in letters)
# find a item exits 'd' in letters: True
print('Index of \'c\' in letters: letters.index(\'c\'): 2' + str(letters.index('c')))
# Index of 'c' in letters: 2
print('count of \'e\' in letters: letters.count(\'e\'): 1' + str(letters.count('e')))
# count of 'e' in letters: 1
print("\n")

#########################################################
# sorting Data Structures
numbers = [5, 2, 9, 1, 5, 6]
print('numbers before sort(): ' + str(numbers))
# numbers before sort(): [5, 2, 9, 1, 5, 6]
numbers.sort()  # Sorting the list
print('numbers after sort(): ' + str(numbers))
# numbers after sort(): [1, 2, 5, 5, 6, 9]

# sort parameters: reverse=True for descending order
numbers.sort(reverse=True)
print('numbers after sort(reverse=True): ' + str(numbers))
# numbers after sort(reverse=True): [9, 6, 5, 5, 2, 1]
numbers.reverse()  # Reversing the list
print('numbers after reverse(): ' + str(numbers))
# numbers after reverse(): [9, 6, 5, 5, 2, 1]
sorted_numbers = sorted(numbers)  # Using sorted() function
print('sorted_numbers using sorted(): ' + str(sorted_numbers))
# sorted_numbers using sorted(): [1, 2, 5, 5, 6, 9]
sorted_numbers = sorted(numbers, reverse=True)  # Descending order
print('sorted_numbers using sorted(reverse=True): ' + str(sorted_numbers))
# sorted_numbers using sorted(reverse=True): [9, 6, 5, 5, 2, 1]

# sort list of tuples based on second element
tuples_list = [(1, 'b'), (3, 'a'), (2, 'c')]
print('tuples_list before sort(): ' + str(tuples_list))
# by calling a function


def sort_by_second_element(item):
    return item[1]


tuples_list.sort(key=sort_by_second_element)
print('tuples_list sorted by second element using function: ' + str(tuples_list))

tuples_list = [(1, 'b'), (2, 'a'), (3, 'c')]
print('tuples_list before sort(): ' + str(tuples_list))
# by lambda function
# by lamda function tuples_list.sort(key=lambda parameters: expression)
tuples_list.sort(key=lambda x: x[1])
print('tuples_list sorted by second element: ' + str(tuples_list))
print("\n")

#########################################################
# Map function to extract items from Data Structures
fruits_prices = [
    ('apple', 23),
    ('banana', 30),
    ('orange', 10)
]
print('fruits_prices: ' + str(fruits_prices))
# fruits_prices: [('apple', 23), ('banana', 30), ('orange', 10)]

# Using map to print fruit names and prices
map(lambda item: print('Fruit: ' +
    item[0] + ', Price: ' + str(item[1])), fruits_prices)
# Fruit: apple, Price: 23
# Fruit: banana, Price: 30
# Fruit: orange, Price: 10

# Extracting prices using map and lambda
prices = list(map(lambda item: item[1], fruits_prices))  # Extracting prices
print(
    'Prices using map and lambda: list(map(lambda parameters: expression, list):' + str(prices))
# Prices using map and lambda: [23, 30, 10]
print("\n")

#########################################################
# Filter function to filter items from Data Structures
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('numbers: ' + str(numbers))
# numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print('Even numbers using filter and lambda: ' + str(even_numbers))
# Even numbers using filter and lambda: [2, 4, 6, 8, 10]

# fruits with price greater than 20
expensive_fruits = list(
    filter(lambda item: item[1] > 20, fruits_prices))
print('Expensive fruits (price > 20): ' + str(expensive_fruits))
# Expensive fruits (price > 20): [('apple', 23), ('banana', 30)]
print("\n")

##########################################################
# List Comprehensions [expression for item in iterable if condition]
squares = [x**2 for x in range(1, 11)]  # Squares of numbers from 1 to 10
print('squares using list comprehension: ' + str(squares))
# squares using list comprehension: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]  # Even squares
print('even_squares using list comprehension: ' + str(even_squares))
# even_squares using list comprehension: [4, 16, 36, 64, 100]
expensive_fruits_names = [
    # Names of expensive fruits
    item[0] for item in fruits_prices if item[1] > 20]
print('Names of expensive fruits using list comprehension: ' +
      str(expensive_fruits_names))
# Names of expensive fruits using list comprehension: ['apple', 'banana']
print("\n")

##########################################################
