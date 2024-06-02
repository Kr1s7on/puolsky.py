# Exercise 2 – GradeConverter (30 min)
# • Create a Python file GradeConverter to read in the marks of a module from the user and
# display the Grade based on the input marks.
# • It will display an error message if the marks is invalid.
# • Assume that there is all the marks are in integer format
# • Draw the flow chart for this
# • Create the program.
# • What are the values you would use to do testing to make sure that your program is running fine?
# Congraduations
# Grade Marks
# A 80-100
# B 70-79
# C 60-69
# D 50-59
# F 0-49
# Test values:
# Test Values Remarks
# -1 , 100 Test invalid values
# 80, 100 Test Grade A
# 70, 79 Test Grade B
# 60, 69 Test Grade C
# 50, 59 Test Grade D
# 1, 49 Test Grade 

# Flowchart
# 1. Start
# 2. Input marks
# 3. Check if the mark is within the range of 0 to 100
# 4. Check if the mark is above 80
# 5. Display "Congratulations! You passed the examination."
# 6. Stop

# ======================================================================================

# Basic Level Solution

# Input mark from user
mark = int(input("Enter your mark: "))

# Check if the mark is within the range of 0 to 100
if 0 <= mark <= 100:
    # Check the grade
    if mark >= 80:
        grade = 'A'
    elif mark >= 70:
        grade = 'B'
    elif mark >= 60:
        grade = 'C'
    elif mark >= 50:
        grade = 'D'
    else:
        grade = 'F'

    # Display the grade
    print(f"Your grade is {grade}.")
else:
    print("Invalid mark. Please enter a number between 0 and 100.")

# ======================================================================================