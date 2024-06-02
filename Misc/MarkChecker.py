# Exercise 1A - MarkCheckerQ1
# Write a program to read an examination mark from the user and display a message if the user passed
# the examination(passing marks is above 60). It will not display anything if the user failed the
# examination.
# Exercise 1C
# 1. Modify the flowchart in Exercise 1B to check that the marks entered is between 0-100.
# 2. If the marks entered is not within the range, an error message will show.
# 3. If the marks entered is within the range, it will proceed.

# Get the mark from the user
mark = int(input("Enter the examination mark: "))
if mark < 0 or mark > 100:
    print("Error: The mark entered is not within the range of 0-100.")
elif mark >= 60:
    print("Congratulations! You passed the examination.")
else:
    print("You failed the examination.")
