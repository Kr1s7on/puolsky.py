# Challenge 1 - Payroll
# Write a payroll program that calculate the monthly pay for hourly employee.
# An hourly employee is paid for the total number of hours they work per month at an hourly rate.
# Use Payroll as the program name.

#  Flowchart
# 1. Start
# 2. Input hourly rate and hours worked
# 3. Calculate monthly pay
# 4. Display the result
# 5. Stop

# ======================================================================================

# Basic Level Solution

# Input hourly rate and hours worked from user
hourly_rate = float(input("Enter hourly rate: "))
hours_worked = float(input("Enter total hours worked in a month: "))

# Calculate monthly pay
monthly_pay = hourly_rate * hours_worked

# Display the result
print(f"The monthly pay is {monthly_pay:.2f}.")

# ======================================================================================

# Advanced Level Solution

# Input hourly rate and hours worked from user
# while True:
#     try:
#         hourly_rate = float(input("Enter hourly rate: "))
#         if hourly_rate <= 0:
#             print("Hourly rate must be a positive number. Please try again.")
#             continue
#         break
#     except ValueError:
#         print("Invalid input. Please enter a number.")

# while True:
#     try:
#         hours_worked = float(input("Enter total hours worked in a month: "))
#         if hours_worked < 0:
#             print("Hours worked cannot be negative. Please try again.")
#             continue
#         break
#     except ValueError:
#         print("Invalid input. Please enter a number.")

# # Calculate monthly pay
# monthly_pay = hourly_rate * hours_worked

# # Display the result
# print(f"The monthly pay is {monthly_pay}.")