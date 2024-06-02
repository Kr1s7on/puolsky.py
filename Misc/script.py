# print statement to print "Hello World!" to the console
print ("Hello World!")

# Either "" or '' can be used to define a string in Python
print ('Hello World!')

# Including quotations
print ('Hello "World!"')

# \n is used to add a new line
print ("Hello \nWorld!")

# \t is used to add a tab space
print ("Hello \tWorld!")

# \b is used to move the cursor one step back
print ("Hello \bWorld!")

# \r is used to move the cursor to the beginning of the line
print ("Hello \rWorld!")

# Types of Errors: Syntax Error, Runtime Error, Logical Error

# Types of variables: int, float, string, boolean

# Example of int variable
my_int = 10
print(my_int)

# Example of float variable
my_float = 3.14
print(my_float)

# Example of string variable
my_string = "Hello World!"
print(my_string)

# Example of boolean variable
my_boolean = True
print(my_boolean)

# Type conversion

# int to float
my_int = 10
my_float = float(my_int)
print(my_float)

# float to int
my_float = 3.14
my_int = int(my_float)
print(my_int)

# int to string
my_int = 10
my_string = str(my_int)
print(my_string)

# float to string
my_float = 3.14
my_string = str(my_float)
print(my_string)

# string to int
my_string = "10"
my_int = int(my_string)
print(my_int)

# string to float
my_string = "3.14"
my_float = float(my_string)
print(my_float)

# string to boolean
my_string = "True"
my_boolean = bool(my_string)
print(my_boolean)

# boolean to string
my_boolean = True
my_string = str(my_boolean)
print(my_string)

# Operators: Arithmetic, Comparison, Logical, Assignment

# Arithmetic Operators: +, -, *, /, %, **, //
# Addition
print (10 + 5)
# Subtraction
print (10 - 5)
# Multiplication
print (10 * 5)
# Division
print (10 / 5)
# Modulus
print (10 % 5)
# Exponent
print (10 ** 5)
# Floor Division
print (10 // 5)

# Comparison Operators: ==, !=, >, <, >=, <=
# Equal to
print (10 == 5)

# Not equal to
print (10 != 5)

# Greater than
print (10 > 5)

# Less than
print (10 < 5)

# Greater than or equal to
print (10 >= 5)

# Less than or equal to
print (10 <= 5)

# Logical Operators: and, or, not
# and
print (10 > 5 and 5 < 10)

# or
print (10 > 5 or 5 > 10)

# not
print (not 10 > 5)

# Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=
# =
x = 10
print (x)
# +=
x += 5
print (x)
# -=
x -= 5
print (x)
# *=
x *= 5
print (x)
# /=
x /= 5
print (x)
# %=
x %= 5
print (x)
# **=
x **= 5
print (x)
# //=
x //= 5
print (x)


# Conditional Statements: if, elif, else

# if
x = 10
if x > 5:
    print ("x is greater than 5")

# if else
x = 10
if x > 5:
    print ("x is greater than 5")
    
else:
    print ("x is less than or equal to 5")

# if elif else
x = 10
if x > 5:
    print ("x is greater than 5")

elif x < 5:
    print ("x is less than 5")

else:
    print ("x is equal to 5")

# Loops: for, while

# for loop
for i in range(5):
    print (i)

# while loop
i = 0
while i < 5:
    print (i)
    i += 1

# Functions

# Defining a function
def my_function():
    print ("Hello World!")

# Calling a function
my_function()

# Function with parameters
def my_function(x):
    print (x)

my_function("Hello World!")

# Function with return value
def my_function(x):
    return x

print (my_function("Hello World!"))

# Function with multiple parameters
def my_function(x, y):
    return x + y

print (my_function(10, 5))

# Function with default parameter
def my_function(x = 10):
    return x

print (my_function())

# Function with variable number of arguments
def my_function(*args):
    return sum(args)

print (my_function(10, 5, 15))

# Function with keyword arguments
def my_function(x, y):
    return x + y

print (my_function(x = 10, y = 5))

# Function with keyword arguments and default parameter
def my_function(x, y = 5):
    return x + y

print (my_function(x = 10))

# Function with keyword arguments and variable number of arguments
def my_function(x, *args):
    return x + sum(args)

print (my_function(10, 5, 15))

# Function with keyword arguments and variable number of keyword arguments
def my_function(x, **kwargs):
    return x + sum(kwargs.values())

print (my_function(10, y = 5, z = 15))

# Function with keyword arguments, variable number of arguments and variable number of keyword arguments
def my_function(x, *args, **kwargs):
    return x + sum(args) + sum(kwargs.values())

print (my_function(10, 5, 15, y = 5, z = 15))


# Classes and Objects

# Defining a class
class MyClass:
    x = 10

# Creating an object of the class
my_object = MyClass()

# Accessing the class variable
print (my_object.x)

# Defining a class with a constructor
class MyClass:
    def __init__(self, x):
        self.x = x

# Creating an object of the class
my_object = MyClass(10)

# Accessing the class variable
print (my_object.x)

# Defining a class with a method
class MyClass:
    def my_method(self):
        return "Hello World!"
    
# Creating an object of the class
my_object = MyClass()

# Calling the method
print (my_object.my_method())
