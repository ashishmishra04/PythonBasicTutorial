# ---------- Comparison Operators ----------
def compare_values(a, b):
    print(f'Comparing {a} and {b}:')
    try:
        print(f'{a} == {b}: {a == b}')  # Equality
        print(f'{a} != {b}: {a != b}')  # Inequality
        print(f'{a} < {b}: {a < b}')    # Less than
        print(f'{a} <= {b}: {a <= b}')  # Less than or equal to
        print(f'{a} > {b}: {a > b}')    # Greater than
        print(f'{a} >= {b}: {a >= b}')  # Greater than or equal to
    except Exception as e:
        print(f'Error comparing values: {e}')


compare_values(5, 10)
# Comparing 5 and 10:
# 5 == 10: False
# 5 != 10: True
# 5 < 10: True
# 5 <= 10: True
# 5 > 10: False
# 5 >= 10: False
compare_values(10, 10)
# Comparing 10 and 10:
# 10 == 10: True
# 10 != 10: False
# 10 < 10: False
# 10 <= 10: True
# 10 > 10: False
# 10 >= 10: True
compare_values(15, 10)
# Comparing 15 and 10:
# 15 == 10: False
# 15 != 10: True
# 15 < 10: False
# 15 <= 10: False
# 15 > 10: True
# 15 >= 10: True
compare_values('apple', 'banana')
# Comparing apple and banana:
# apple == banana: False
# apple != banana: True
# apple < banana: True
# apple <= banana: True
# apple > banana: False
# apple >= banana: False
compare_values('banana', 'banana')
# Comparing banana and banana:
# banana == banana: True
# banana != banana: False
# banana < banana: False
# banana <= banana: True
# banana > banana: False
# banana >= banana: True
compare_values('cherry', 'banana')
# Comparing cherry and banana:
# cherry == banana: False
# cherry != banana: True
# cherry < banana: False
# cherry <= banana: False
# cherry > banana: True
# cherry >= banana: True
compare_values(5, 5.0)  # Comparing int and float
# Comparing 5 and 5.0:
# 5 == 5.0: True
# 5 != 5.0: False
# 5 < 5.0: False
# 5 <= 5.0: True
# 5 > 5.0: False
# 5 >= 5.0: True
compare_values(5.0, 5)  # Comparing float and int
# Comparing 5.0 and 5:
# 5.0 == 5: True
# 5.0 != 5: False
# 5.0 < 5: False
# 5.0 <= 5: True
# 5.0 > 5: False
# 5.0 >= 5: True
compare_values(5, None)  # Comparing with None
# Comparing 5 and None:
# 5 == None: False
# 5 != None: True
# Error comparing values: '<' not supported between instances of 'int' and 'NoneType'
compare_values(None, 5)  # Comparing with None
# Comparing None and 5:
# None == 5: False
# None != 5: True
# Error comparing values: '<' not supported between instances of 'NoneType' and 'int'
compare_values(None, None)  # Comparing None with None
# Comparing None and None:
# None == None: True
# None != None: False
# Error comparing values: '<' not supported between instances of 'NoneType' and 'NoneType'
compare_values(True, False)  # Comparing booleans
# Comparing True and False:
# True == False: False
# True != False: True
# True < False: False
# True <= False: False
# True > False: True
# True >= False: True
compare_values(False, True)  # Comparing booleans
# Comparing False and True:
# False == True: False
# False != True: True
# False < True: True
# False <= True: True
# False > True: False
# False >= True: False
compare_values(True, True)  # Comparing booleans
# Comparing True and True:
# True == True: True
# True != True: False
# True < True: False
# True <= True: True
# True > True: False
# True >= True: True
compare_values(False, False)  # Comparing booleans
# Comparing False and False:
# False == False: True
# False != False: False
# False < False: False
# False <= False: True
# False > False: False
# False >= False: True
compare_values(True, 1)  # Comparing boolean and int
# Comparing True and 1:
# True == 1: True
# True != 1: False
# True < 1: False
# True <= 1: True
# True > 1: False
# True >= 1: True
compare_values(False, 0)  # Comparing boolean and int
# Comparing False and 0:
# False == 0: True
# False != 0: False
# False < 0: False
# False <= 0: True
# False > 0: False
# False >= 0: True
compare_values('apple', 5)  # Comparing different types
# Comparing apple and 5:
# apple == 5: False
# apple != 5: True
# Error comparing values: '<' not supported between instances of 'str' and 'int'
compare_values(5, 'apple')  # Comparing different types
# Comparing 5 and apple:
# 5 == apple: False
# 5 != apple: True
# Error comparing values: '<' not supported between instances of 'int' and 'str'
print("\n")

# ---------- Conditional Statements ----------


def check_number(num):
    if num > 0:
        print(f'{num} is positive.')
    elif num < 0:
        print(f'{num} is negative.')
    else:
        print(f'{num} is zero.')


check_number(10)  # 10 is positive.
check_number(-5)  # -5 is negative.
check_number(0)   # 0 is zero.
check_number(3.5)  # 3.5 is positive.
check_number(-2.7)  # -2.7 is negative.
check_number(0.0)  # 0.0 is zero.
check_number(-0.0)  # -0.0 is zero.
print("\n")
# If-ElseIf-Else with Strings


def check_fruit(fruit):
    if fruit == 'apple':
        print('This is an apple.')
    elif fruit == 'banana':
        print('This is a banana.')
    elif fruit == 'cherry':
        print('This is a cherry.')
    else:
        print('Unknown fruit.')


check_fruit('apple')   # This is an apple.
check_fruit('banana')  # This is a banana.
check_fruit('cherry')  # This is a cherry.
check_fruit('date')    # Unknown fruit.
print("\n")
# Nested If Statements


def check_age_and_membership(age, is_member):
    if age >= 18:
        if is_member:
            print('Adult member.')
        else:
            print('Adult non-member.')
    else:
        if is_member:
            print('Minor member.')
        else:
            print('Minor non-member.')


check_age_and_membership(20, True)   # Adult member.
check_age_and_membership(20, False)  # Adult non-member.
check_age_and_membership(16, True)   # Minor member.
print("\n")

# Ternary Operator


def check_even_odd(num):
    result = 'Even' if num % 2 == 0 else 'Odd'
    print(f'{num} is {result}.')


check_even_odd(4)  # 4 is Even.
check_even_odd(7)  # 7 is Odd.
check_even_odd(0)  # 0 is Even.
print("\n")

# Logical Operators and, or, not


def check_access(age, has_permission):
    if age >= 18 and has_permission:
        print('Access granted.')
    elif age < 18 and has_permission:
        print('Access denied: Underage.')
    elif age >= 18 and not has_permission:
        print('Access denied: No permission.')
    else:
        print('Access denied: Underage and no permission.')


check_access(20, True)   # Access granted.
check_access(16, True)   # Access denied: Underage.
check_access(20, False)  # Access denied: No permission.
check_access(16, False)  # Access denied: Underage and no permission.
print("\n")


# short-circuit evaluation
def safe_divide(a, b):
    if b != 0 and (result := a / b) > 1:  # Using walrus operator for assignment
        print(f'Result is greater than 1: {result}')
    elif b == 0:
        print('Cannot divide by zero.')
    else:
        print(f'Result is {result}')


safe_divide(10, 2)  # Result is greater than 1: 5.0
safe_divide(1, 2)   # Result is 0.5
safe_divide(10, 0)  # Cannot divide by zero.
safe_divide(0, 5)   # Result is 0.0
print("\n")

# Chaining Comparison Operators


def check_range(num):
    if 0 < num < 10:  # same as if num > 0 and num < 10
        print(f'{num} is between 0 and 10.')
    elif num <= 0:
        print(f'{num} is less than or equal to 0.')
    else:
        print(f'{num} is greater than or equal to 10.')


check_range(5)    # 5 is between 0 and 10.
check_range(-3)   # -3 is less than or equal to 0.
print("\n")

# For Loops with else


def find_even_number(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f'Found an even number: {num}')
            break  # Exit loop if even number is found
    else:
        print('No even number found.')


find_even_number([1, 3, 5, 7])        # No even number found.
find_even_number([1, 3, 4, 5, 7])     # Found an even number: 4
find_even_number([2, 4, 6, 8])        # Found an even number: 2
find_even_number([])                   # No even number found.
print("\n")
# While Loops with else


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    else:
        print('Countdown finished!')


countdown(5)  # 5 4 3 2 1 Countdown finished!
countdown(0)  # Countdown finished!
countdown(-3)  # Countdown finished!
print("\n")

# nested loops with break and continue


def print_matrix(matrix):
    for row in matrix:  # parent loop
        for value in row:  # child loop
            if value < 0:
                print('Negative value encountered, stopping inner loop.')
                break  # Exit inner loop on negative value
            if value == 0:
                print('Zero value encountered, skipping this value.')
                continue  # Skip zero values
            print(value, end=' ')
        else:
            print('Completed a row without encountering a negative value.')
        print()  # New line after each row


print_matrix([[1, 2, 3], [4, 0, 6], [7, -8, 9]])
# 1 2 3
# Completed a row without encountering a negative value.
# 4 Zero value encountered, skipping this value.
# 6
# Completed a row without encountering a negative value.
# Negative value encountered, stopping inner loop.
print_matrix([[0, 0, 0], [1, 2, 3], [4, 5, 6]])
# Zero value encountered, skipping this value.
# Zero value encountered, skipping this value.
# Zero value encountered, skipping this value.
# Completed a row without encountering a negative value.
# 1 2 3
# Completed a row without encountering a negative value.
# 4 5 6
# Completed a row without encountering a negative value.
print("\n")
