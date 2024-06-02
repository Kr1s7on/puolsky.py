# Exercise 2A - TicketSales
# Write a program to help the ticketing staff to calculate ticket price at the ticketing counter.
# During weekdays, customers who have corporate membership will enjoy a 20% discount on the total ticket price whereas customers who have family membership will have free entry for all children.
# During weekends, the ticket price for both child and adult are fixed at $10 regardless of whether any membership is presented.
# You do not need to format the decimal places for the price.
# Your program should generate the following output with the following sample inputs.

# Ticket Type Price
# Child $7.50
# Adult $10

# Your program should generate the following output with the following sample inputs.
# Samples output 1(User inputs are shown in bold)
# Enter day : 5
# Enter number of child ticket: 2
# Enter number of adult ticket: 2
# Enter Membership (C)orporate/(F)amily/(N)o: C
# Please pay $28.0
# Samples output 2(User inputs are shown in bold)
# Enter day : 4
# Enter number of child ticket: 3
# Enter number of adult ticket: 2
# Enter Membership (C)orporate/(F)amily/(N)o: F
# Please pay $20
# Samples output 3(User inputs are shown in bold) Enter day : 2
# Enter number of child ticket: 4
# Enter number of adult ticket: 3
# Enter Membership (C)orporate/(F)amily/(N)o: N
# Please pay $60.0
# Samples output 4(User inputs are shown in bold)
# Enter day : 7
# Enter number of child ticket: 4
# Enter number of adult ticket: 4
# Enter Membership (C)orporate/(F)amily/(N)o: F
# Please pay $80
# Samples output 5(User inputs are shown in bold)
# Enter day : 0 Incorrect day!
# Samples output 6(User inputs are shown in bold)
# Enter day : 8 Incorrect day!

# Get the day from the user
day = int(input("Enter day : "))
if day < 1 or day > 7:
    print("Incorrect day!")