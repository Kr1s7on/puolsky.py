# Challenge 2 - InfoDisplay
# Create a program to prompt user for information and display the information on screen.
# A sample run of the program is as shown. Use InfoDisplay as the program name.
# Draw the flow chart for this program and
# Next proceed to create the program.

# BMI formular:
# weight(kg) /(height(cm) X height(cm))

# Flowchart
# 1. Start
# 2. Input name, age, weight and height
# 3. Calculate BMI
# 4. Display the information
# 5. Stop

# ======================================================================================

# Basic Level Solution

# Input name, age, weight and height from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

# Convert height from cm to m
height = height / 100

# Calculate BMI
bmi = weight / (height * height)

# Display the information
print(f"Your name is {name}.")
print(f"Your age is {age}.")
print(f"Your weight is {weight} kg.")
print(f"Your height is {height} m.")
print(f"Your BMI is {bmi}.")

# ======================================================================================