# Challenge 3
# • For ITB511 Programming, there are 2 practical tests, 1 practical assignment and one quiz which sum up
# the final marks.
# • You are tasked to calculate the total mark
# ICA          Base Marks      Weightage
# Quiz         10              10%
# Practical
# Test 1 & 2   100 each        30% each
# Practical
# Assignment   100             30%

# Flowchart
# 1. Start
# 2. Input marks for quiz, practical test 1, practical test 2 and practical assignment
# 3. Calculate total mark
# 4. Display the result
# 5. Stop

# ======================================================================================

# Basic Level Solution

# Input marks from user
quiz_mark = float(input("Enter your Quiz mark out of 10: "))
practical_test1_mark = float(input("Enter your Practical Test 1 mark out of 100: "))
practical_test2_mark = float(input("Enter your Practical Test 2 mark out of 100: "))
practical_assignment_mark = float(input("Enter your Practical Assignment mark out of 100: "))

# Calculate total mark
total_mark = (quiz_mark * 0.1) + (practical_test1_mark * 0.3) + (practical_test2_mark * 0.3) + (practical_assignment_mark * 0.3)

# Display the result
print(f"Your total mark is {total_mark}.")

# ======================================================================================
