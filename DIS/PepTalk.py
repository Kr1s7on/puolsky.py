list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def calc_sum(x, y):
    """Calculate sum of two numbers."""
    return x + y

def calc_product(x, y):
    """Calculate product of two numbers."""
    return x * y

def calc_difference(x, y):
    """Calculate difference between two numbers."""
    return x - y

def calc_quotient(x, y):
    """Calculate quotient of two numbers."""
    if y == 0:
        print("Error: Cannot divide by zero.")  # Error message if user tries to divide by zero
        return None
    else:
        return x / y

# Calculate the sum of the first two numbers in the list
TOTAL_SUM = calc_sum(list_of_numbers[0], list_of_numbers[1])
print("Total Sum:", TOTAL_SUM)

# Calculate the product of the third and fourth numbers in the list
TOTAL_PRODUCT = calc_product(list_of_numbers[2], list_of_numbers[3])
print("Total Product:", TOTAL_PRODUCT)

# Calculate the difference between the fifth and sixth numbers in the list
TOTAL_DIFFERENCE = calc_difference(list_of_numbers[4], list_of_numbers[5])
print("Total Difference:", TOTAL_DIFFERENCE)

# Calculate the quotient of the seventh and eighth numbers in the list
TOTAL_QUOTIENT = calc_quotient(list_of_numbers[6], list_of_numbers[7])
print("Total Quotient:", TOTAL_QUOTIENT)
