# Challenge 1 - Payroll
# Write a payroll program that calculate the monthly pay for hourly employee.
# An hourly employee is paid for the total number of hours they work per month at an hourly rate.
# Use Payroll as the program name.

name = input("Enter your name: ")

hours = float(input("Enter the number of hours you worked this month: "))

rate = float(input("Enter your hourly rate: "))

pay = hours * rate

print("Hello, " + name + "! Your pay for this month is $" + str(pay) + ".")

