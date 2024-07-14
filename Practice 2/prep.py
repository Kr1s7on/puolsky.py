# ================================
# Prepared Cheatsheet for Test 2
# ================================

# Lists
# ==========================================================
# Lists (ordered, mutable collections)
my_list = [1, 2, 3, "apple", "banana"]

# Accessing elements:
first_element = my_list[0]  # Accesses the first element (index 0)
last_element = my_list[-1]  # Accesses the last element

# Slicing (extracting a portion of the list):
sub_list = my_list[1:3]  # Extracts elements from index 1 (inclusive) to 3 (exclusive)

# Modifying lists:
my_list.append(new_item)  # Adds an item to the end
my_list.insert(index, item)  # Inserts an item at a specific index
my_list.remove(item)  # Removes the first occurrence of an item
my_list.pop(index)  # Removes and returns the item at a specific index (or the last item if no index)
my_list.sort()  # Sorts the list in ascending order
my_list.reverse()  # Reverses the order of the list

# List comprehension:
squared = [x**2 for x in my_list]  # Creates a new list with squared elements
filtered = [x for x in my_list if x > 2]  # Creates a new list with elements greater than 2

# Common list operations:
list_concatenation = my_list + [4, 5]  # Combines two lists
list_repetition = my_list * 2  # Repeats the list elements
list_length = len(my_list)  # Returns the number of elements in the list

# Converting between lists and strings:
my_string = "Hello"
my_list = list(my_string)  # Converts a string to a list of characters
my_string = "".join(my_list)  # Converts a list of characters to a string

# Note: Lists are versatile and can store different types of data
# ==========================================================




# Tuples
# ==========================================================
# Tuples (ordered, immutable collections)
my_tuple = (1, 2, 3, "apple")  # Tuples cannot be modified after creation

# Accessing elements:
first_element = my_tuple[0]  # Accesses the first element (index 0)

# Unpacking tuples:
a, b, c, d = my_tuple  # Assigns each element to a separate variable

# Common tuple operations:
tuple_concatenation = my_tuple + (4, 5)  # Combines two tuples
tuple_repetition = my_tuple * 2  # Repeats the tuple elements

# Converting between lists and tuples:
my_list = list(my_tuple)  # Converts a tuple to a list
my_tuple = tuple(my_list)  # Converts a list to a tuple

# Note: Tuples are commonly used for returning multiple values from functions
# ==========================================================




# Dictionaries
# ==========================================================
# Dictionaries (unordered, key-value pairs)
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing values:
value = my_dict["name"]  # Accesses the value associated with the key "name"

# Checking for keys:
if "age" in my_dict:
    # Do something if the key exists in the dictionary

# Common dictionary operations:
keys = my_dict.keys()  # Returns a list of keys
values = my_dict.values()  # Returns a list of values
items = my_dict.items()  # Returns a list of key-value pairs

# Modifying dictionaries:
my_dict["age"] = 31  # Updates the value for an existing key
my_dict["new_key"] = "New value"  # Adds a new key-value pair
del my_dict["city"]  # Removes a key-value pair

# Dictionary comprehension:
squared_dict = {x: x**2 for x in range(5)}  # Creates a dictionary with squared values

# Note: Dictionaries are useful for mapping keys to values
# ==========================================================




# Sets
# ==========================================================
# Sets (unordered, unique elements)
my_set = {1, 2, 3, "apple", "apple"}  # Duplicates are automatically removed

# Common Set Operations:
union = my_set | {4, 5}  # Combines elements from both sets (no duplicates)
intersection = my_set & {2, "apple"}  # Elements present in both sets
difference = my_set - {1}  # Elements in my_set but not in the other set

# Set Comprehension:
squared_set = {x**2 for x in range(5)}  # Creates a set with squared elements

# Note: Sets are useful for storing unique elements and performing set operations
# ==========================================================




# Flow Statements
# ==========================================================
# Control Flow Statements

# Conditional statements (if, elif, else):
if condition:
    # Do something if the condition is true
elif another_condition:
    # Do something if the first condition is false and this condition is true
else:
    # Do something if none of the above conditions are true

# For loops (iterate over a sequence of items):
for item in sequence:
    # Do something with the item

# While loops (continue looping as long as a condition is true):
while condition:
    # Do something
    # Don't forget to update the condition to avoid an infinite loop

# Loop control statements:
break  # Exit the loop immediately
continue  # Skip the rest of the code block and continue with the next iteration

# Nested loops (loops within loops):
for x in range(5):
    for y in range(3):
        # Do something with x and y

# Looping through dictionaries:
for key, value in my_dict.items():
    # Access both the key and value in each iteration

# Looping with an index:
for index, item in enumerate(my_list):
    # Access both the index and item in each iteration

# List comprehension with conditionals:
filtered = [x for x in my_list if x > 2]  # Creates a new list with elements greater than 2

# Note: Flow statements control the execution of code based on conditions and loops
# ==========================================================




# Functions
# ==========================================================
# Functions (reusable blocks of code)

def function_name(parameters):
    # Do something with the parameters
    return value  # Optional: return a value

# Calling a function:
result = function_name(arguments)  # Pass arguments to the function

# Default arguments:
def greet(name="Alice"):
    return f"Hello, {name}!"

# Variable-length arguments:
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

# Keyword arguments:
def person(name, age):
    return f"Name: {name}, Age: {age}"

# Lambda functions (anonymous functions):
square = lambda x: x**2  # Equivalent to def square(x): return x**2

# Note: Functions help organize code into reusable blocks and improve readability
# ==========================================================




# Strings
# ==========================================================
# String Manipulation

# Creating strings:
my_string = "Hello, world!"

# String formatting (f-strings):
name = "Alice"
age = 30
greeting = f"Hello, {name}! You are {age} years old."

# String slicing (extracting a portion of the string):
sub_string = my_string[1:7]  # Extracts characters from index 1 (inclusive) to 7 (exclusive)

# Common string methods:
lower_case = my_string.lower()  # Converts all characters to lowercase
upper_case = my_string.upper()  # Converts all characters to uppercase
split_words = my_string.split()  # Splits the string into a list of words

# String concatenation:
new_string = "Hello" + " " + "World"  # Combines two strings

# String interpolation:
formatted_string = "Value: {:.2f}".format(3.14159)  # Formats the string with 2 decimal places

# Note: Strings are sequences of characters and support various operations
# ==========================================================




# Files
# ==========================================================
# File I/O

# Opening a file:
with open("filename.txt", "r") as file:
    # Read content from the file

# Writing to a file:
with open("filename.txt", "w") as file:
    file.write("This is a new line of text.")

# Appending to a file:
with open("filename.txt", "a") as file:
    file.write("This is another line of text.")

# Reading from a file:
with open("filename.txt", "r") as file:
    content = file.read()

# Note: File I/O operations allow reading from and writing to files
# ==========================================================




# Errors
# ==========================================================
# Exception Handling
try:
    # Code that might raise an exception
except ExceptionType:
    # Handle the exception
# Error Types: ValueError, TypeError, IndexError, KeyError, FileNotFoundError, etc.

# Or you can define specific exceptions to catch:
except ValueError as e:
    # Handle a specific type of exception
    print(f"ValueError: {e}")
finally:
    # Code that will always run, regardless of whether an exception occurred

# Raising exceptions:
if condition:
    raise ExceptionType("Error message")

# Exception Types:
# - ValueError: Raised when a function receives an argument of the correct type but an inappropriate value
# - TypeError: Raised when an operation or function is applied to an object of inappropriate type
# - IndexError: Raised when an index is out of range
# - KeyError: Raised when a dictionary key is not found
# - FileNotFoundError: Raised when a file is not found

# Custom Exceptions:
class CustomError(Exception):
    pass

# Raise a custom exception:
raise CustomError("An error occurred")

# Note: Exception handling helps manage errors and prevent program crashes
# ==========================================================




# Classes
# ==========================================================
# Classes (blueprints for creating objects)

class ClassName:
    def __init__(self, parameters):
        # Constructor method (initialize object attributes)
        self.attribute = parameters

    def method_name(self, arguments):
        # Class method
        return value
    
    @staticmethod
    def static_method(arguments):
        # Static method (no access to class or instance
        return value
# ==========================================================
# Note: This is a general overview of key concepts and syntax.




# Example Usage:
# ==========================================================
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Define a function to calculate the sum of a list
def calculate_sum(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

# Call the function with the list of numbers
result = calculate_sum(numbers)
print(result)  # Output: 15



# Create a dictionary of student names and marks
students = {
    "Alice": 85,
    "Bob": 75,
    "Charlie": 90
}

# Define a function to calculate the average marks
def calculate_average(marks_dict):
    total = sum(marks_dict.values())
    count = len(marks_dict)
    return total / count

# Call the function with the dictionary of marks
average = calculate_average(students)
print(average)  # Output: 83.33



# Create a string
my_string = "Hello, World!"

# Use string methods to convert to uppercase
upper_case = my_string.upper()
print(upper_case)  # Output: HELLO, WORLD!


    
# Create an instance of the Person class
alice = Person("Alice", 30)

# Call the greet method of the instance
greeting = alice.greet()
print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.
# ==========================================================

# End of Cheatsheet