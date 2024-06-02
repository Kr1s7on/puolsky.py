# Exercise 3 - ATMDispenser
# Write a program to simulate an ATM machine to dispense correct number of $50 and
# $10 notes according to the withdrawal amount enter at the machine.
# • The withdrawal amount must be greater than zero and in multiple of 10.
# • Assume there is an infinite supply of notes. The output is to display number of $50
# notes and $10 to dispense.
# Your program should generate the following output with the following sample inputs.

# Hint: use % and //

# Samples output 1(User inputs are shown in bold)
# Enter withdrawal amount : 0
# Please enter a valid withdrawal amount
# Samples output 2(User inputs are shown in bold)
# Enter withdrawal amount : 11
# Please enter withdrawal amount in multiple of 10
# Samples output 3(User inputs are shown in bold)
# Enter withdrawal amount : 20
# Number of $10 note dispensed is 2
# Samples output 4(User inputs are shown in bold)
# Enter withdrawal amount : 100
# Number of $50 note dispensed is 2
# Samples output 5(User inputs are shown in bold)
# Enter withdrawal amount : 1230
# Number of $50 note dispensed is 24
# Number of $10 note dispensed is 3

# Flowchart
# 1. Start
# 2. Input withdrawal amount
# 3. Check if the amount is greater than zero
# 4. Check if the amount is in multiple of 10
# 5. Calculate the number of $50 notes to dispense
# 6. Calculate the number of $10 notes to dispense
# 7. Display the number of $50 and $10 notes to dispense
# 8. Stop

# ======================================================================================

# Basic Level Solution

# Input withdrawal amount
amount = int(input("Enter withdrawal amount: "))

# Check if the amount is valid
if amount <= 0:
    print("Please enter a valid withdrawal amount")
elif amount % 10 != 0:
    print("Please enter withdrawal amount in multiple of 10")
else:
    # Calculate the number of $50 and $10 notes to dispense
    notes_50 = amount // 50
    amount %= 50
    notes_10 = amount // 10

    # Display the number of $50 and $10 notes to dispense
    if notes_50 > 0:
        print(f"Number of $50 note dispensed is {notes_50}")
    if notes_10 > 0:
        print(f"Number of $10 note dispensed is {notes_10}")

# ======================================================================================
