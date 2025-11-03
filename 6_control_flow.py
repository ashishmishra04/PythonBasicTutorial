# ==========================================================
# ---------- Comparison Operators ----------
# ==========================================================
def compare_values(a, b):
    print(f'Comparing {a} and {b}:')
    try:
        print(f'{a} == {b}: {a == b}')   # Equality
        print(f'{a} != {b}: {a != b}')   # Inequality
        print(f'{a} < {b}: {a < b}')     # Less than
        print(f'{a} <= {b}: {a <= b}')   # Less than or equal to
        print(f'{a} > {b}: {a > b}')     # Greater than
        print(f'{a} >= {b}: {a >= b}')   # Greater than or equal to
    except Exception as e:
        print(f'Error comparing values: {e}')


# Integer comparisons
compare_values(5, 10)
compare_values(10, 10)
compare_values(15, 10)

# String comparisons
compare_values('apple', 'banana')
compare_values('banana', 'banana')
compare_values('cherry', 'banana')

# Mixed numeric types
compare_values(5, 5.0)
compare_values(5.0, 5)

# Comparisons with None
compare_values(5, None)
compare_values(None, 5)
compare_values(None, None)

# Boolean comparisons
compare_values(True, False)
compare_values(False, True)
compare_values(True, True)
compare_values(False, False)

# Booleans vs integers
compare_values(True, 1)
compare_values(False, 0)

# Comparing different types
compare_values('apple', 5)
compare_values(5, 'apple')
print("\n")


# ==========================================================
# ---------- Conditional Statements ----------
# ==========================================================
def check_number(num):
    if num > 0:
        print(f'{num} is positive.')
    elif num < 0:
        print(f'{num} is negative.')
    else:
        print(f'{num} is zero.')


check_number(10)
check_number(-5)
check_number(0)
check_number(3.5)
check_number(-2.7)
check_number(0.0)
check_number(-0.0)
print("\n")


# ==========================================================
# If-ElseIf-Else with Strings
# ==========================================================
def check_fruit(fruit):
    if fruit == 'apple':
        print('This is an apple.')
    elif fruit == 'banana':
        print('This is a banana.')
    elif fruit == 'cherry':
        print('This is a cherry.')
    else:
        print('Unknown fruit.')


check_fruit('apple')
check_fruit('banana')
check_fruit('cherry')
check_fruit('date')
print("\n")


# ==========================================================
# Nested If Statements
# ==========================================================
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


check_age_and_membership(20, True)
check_age_and_membership(20, False)
check_age_and_membership(16, True)
print("\n")


# ==========================================================
# Ternary Operator
# ==========================================================
def check_even_odd(num):
    result = 'Even' if num % 2 == 0 else 'Odd'
    print(f'{num} is {result}.')


check_even_odd(4)
check_even_odd(7)
check_even_odd(0)
print("\n")


# ==========================================================
# Logical Operators: and, or, not
# ==========================================================
def check_access(age, has_permission):
    if age >= 18 and has_permission:
        print('Access granted.')
    elif age < 18 and has_permission:
        print('Access denied: Underage.')
    elif age >= 18 and not has_permission:
        print('Access denied: No permission.')
    else:
        print('Access denied: Underage and no permission.')


check_access(20, True)
check_access(16, True)
check_access(20, False)
check_access(16, False)
print("\n")


# ==========================================================
# Short-circuit evaluation + Walrus operator
# ==========================================================
def safe_divide(a, b):
    if b != 0 and (result := a / b) > 1:
        print(f'Result is greater than 1: {result}')
    elif b == 0:
        print('Cannot divide by zero.')
    else:
        print(f'Result is {result}')


safe_divide(10, 2)
safe_divide(1, 2)
safe_divide(10, 0)
safe_divide(0, 5)
print("\n")


# ==========================================================
# Chaining Comparison Operators
# ==========================================================
def check_range(num):
    if 0 < num < 10:  # same as if num > 0 and num < 10
        print(f'{num} is between 0 and 10.')
    elif num <= 0:
        print(f'{num} is less than or equal to 0.')
    else:
        print(f'{num} is greater than or equal to 10.')


check_range(5)
check_range(-3)
print("\n")


# ==========================================================
# For Loops with else
# ==========================================================
def find_even_number(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f'Found an even number: {num}')
            break
    else:
        print('No even number found.')


find_even_number([1, 3, 5, 7])
find_even_number([1, 3, 4, 5, 7])
find_even_number([2, 4, 6, 8])
find_even_number([])
print("\n")


# ==========================================================
# While Loops with else
# ==========================================================
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    else:
        print('Countdown finished!')


countdown(5)
countdown(0)
countdown(-3)
print("\n")


# ==========================================================
# Nested loops with break and continue
# ==========================================================
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                print('Negative value encountered, stopping inner loop.')
                break
            if value == 0:
                print('Zero value encountered, skipping this value.')
                continue
            print(value, end=' ')
        else:
            print('Completed a row without encountering a negative value.')
        print()


print_matrix([[1, 2, 3], [4, 0, 6], [7, -8, 9]])
print_matrix([[0, 0, 0], [1, 2, 3], [4, 5, 6]])
print("\n")
