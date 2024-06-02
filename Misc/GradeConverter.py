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

def grade_converter():
    mark = int(input("Enter the examination mark: "))
    if mark < 0 or mark > 100:
        print("Error: The mark entered is not within the range of 0-100.")
    elif mark >= 80:
        print("Congratulations! You passed the examination with Grade A.")
    elif mark >= 70:
        print("Congratulations! You passed the examination with Grade B.")
    elif mark >= 60:
        print("Congratulations! You passed the examination with Grade C.")
    elif mark >= 50:
        print("Congratulations! You passed the examination with Grade D.")
    else:
        print("You failed the examination with Grade F.")
