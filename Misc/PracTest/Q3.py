# ======================================================================================

# Author: Kriston Jomari
# Admin No: 231165R

# ======================================================================================

# Write a program that:
# - asks the user to enter a start number and an end number.
# - finds all the numbers that are not multiples of 5 between the start and the end number (inclusive) and total up the numbers.
# - displays the total.

# Enter start number: 3
# Enter end number: 12
# 60
# 3 4 6 7 8 9 11 12
# ======================================================================================

# start_number = int(input("Enter start number: "))
# end_number = int(input("Enter end number: "))

# for i in range(start_number, end_number):
#     i = i + (i // 5 != 0)
#     print(i)

start_number = int(input("Enter start number: "))
end_number = int(input("Enter end number: "))

total = 0
for i in range(start_number, end_number + 1):
    if i % 5 != 0:
        total += i

print("Total:", total)