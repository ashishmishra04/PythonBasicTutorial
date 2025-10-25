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
print("\n")

#########################################################
# find items in Data Structures
print('Is \'a\' in letters? ' + str('a' in letters))
# Is 'a' in letters? True
