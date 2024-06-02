# Exercise 1ABC - MarkCheckerQ1
# Write a program to read an examination mark from the user and display a message if the user passed
# the examination(passing marks is above 60). It will not display anything if the user failed the
# examination.
# Complete the flowchart before writing the Python codes. Use MarkCheckerQ1 as the file name

# Output
# Enter your examination mark: 70
# Congratulations! You passed the examination.

# Flowchart
# 1. Start
# 2. Input examination mark
# 3. Check if the mark is above 60
# 4. Display "Congratulations! You passed the examination."
# 5. Stop

# ======================================================================================

# Basic Level Solution

# Input examination mark from user
examination_mark = float(input("Enter your examination mark: "))

# Check if the mark is within the range of 0 to 100
if examination_mark < 0 or examination_mark > 100:
    print("Invalid mark. Please enter a number between 0 and 100.")
else:
    # Check if the mark is above 60
    if examination_mark > 60:
        # Display a message
        print("Congratulations! You passed the examination.")

# ======================================================================================

# Advanced Level Solution

# def get_examination_mark():
#     while True:
#         try:
#             mark = float(input("Enter your examination mark: "))
#             if 0 <= mark <= 100:
#                 return mark
#             else:
#                 print("Invalid mark. Please enter a number between 0 and 100.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# # Input examination mark from user
# examination_mark = get_examination_mark()

# # Check if the mark is above 60
# if examination_mark > 60:
#     # Display a message
#     print("Congratulations! You passed the examination.")

# ======================================================================================
