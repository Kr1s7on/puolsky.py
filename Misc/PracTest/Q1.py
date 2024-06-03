# ======================================================================================

# Author: Kriston Jomari
# Admin No: 231165R

# ======================================================================================

# Question 1 (15 points)
# Write a program that prompts the user to enter his exam score and displays the corresponding message.
# Your program should use if, elif and else statements to determine the appropriate message.
# Note: You can assume that user will only input valid exam scores between 0 and 100, inclusive.


# Enter your exam score   Message
# Below 60    You failed this exam.
# Between 60 and 90 (inclusive)   You passed this exam.
# More than 90    You passed this exam with distinction.

# ======================================================================================

# Asks user for score
score = int(input("Enter your exam score: "))

# Checks if score is within valid range of 0 to 100
if score < 0 or score > 100:
    print("Invalid mark. Please enter a number between 0 and 100.")
else:
    if score > 90:  # More than 90
        print("You passed this exam with distinction.")
    elif score <= 90 and score >= 60:   # Normal pass
        print("You passed this exam.")
    else:   # Fail
        print("You failed this exam.")

# ======================================================================================