# Exercise 4
# 1. Your cumulative grade point average (GPA) is calculated by dividing the total amount of grade points
# earned by the total amount of credits. Your GPA may range from 0.0 to a 4.0. To get the student's
# cumulative GPA, the total grade points are divided by the total credit points. Given the example
# table of credit and grade points below, the GPA is calculated by using this formula
# GPA = (3.5*4+3.5*4+3*4+2*8+4*2) / (4+4+4+8+2) = 2.91
# Module Code Credit Grade Point Average Grade Point
# Module 1 4 3.5 3.5 * 4
# Module 2 4 3.5 3.5 * 4
# Module 3 4 3 3 * 4
# Module 4 8 2 2 * 8
# Module 5 2 4 4 * 2
# a) Write a program using for-loop to prompt the user to enter the credit, GPA
# for the 5 modules, and print out its cumulative GPA for the 5 modules.

# Sample Output:
# Enter the credit for Module 1: 4
# Enter your GPA for Module 1: 3.5
# Enter the credit for Module 2: 4
# Enter your GPA for Module 2: 3.5
# Enter the credit for Module 3: 4
# Enter your GPA for Module 3: 3
# Enter the credit for Module 4: 8
# Enter your GPA for Module 4: 2
# Enter the credit for Module 5: 2
# Enter your GPA for Module 5: 4
# Your cumulative GPA for 5 modules are 2.909090909090909

# Flowchart
# 1. Start
# 2. Initialize total_credit to 0
# 3. Initialize total_grade to 0
# 4. Loop through 5 modules
# 5. Input credit for the module
# 6. Input GPA for the module
# 7. Calculate grade points for the module
# 8. Calculate total credit points
# 9. Calculate total grade points
# 10. Calculate cumulative GPA
# 11. Display cumulative GPA
# 12. Stop

# ======================================================================================

# Basic Level Solution

# Initialize total_credit to 0
total_credit = 0
# Initialize total_grade to 0
total_grade = 0

# Loop through 5 modules
for i in range(1, 6):
    # Input credit for the module
    credit = int(input(f"Enter the credit for Module {i}: "))
    # Input GPA for the module
    gpa = float(input(f"Enter your GPA for Module {i}: "))
    
    # Calculate grade points for the module
    grade_points = credit * gpa
    
    # Calculate total credit points
    total_credit += credit
    # Calculate total grade points
    total_grade += grade_points

# Calculate cumulative GPA
cumulative_gpa = total_grade / total_credit

# Display cumulative GPA
print(f"Your cumulative GPA for 5 modules is {cumulative_gpa}")

# ======================================================================================