# Exercise 2AB - TicketSales
# Write a program to help the ticketing staff to calculate ticket price at the ticketing
# counter.
# During weekdays, customers who have corporate membership will enjoy a 20%
# discount on the total ticket price whereas customers who have family
# membership will have free entry for all children.
# During weekends, the ticket price for both child and adult are fixed at $10
# regardless of whether any membership is presented.
# Your program should generate the following output with the following sample inputs.
# Modify the codes so that it can accept upper and lower case for (C)oporate and (F)amily.

# Ticket Type Price
# Child $7.50
# Adult $10

# Flowchart
# 1. Start
# 2. Input ticket type and quantity
# 3. Check if it is a weekday
# 4. Check if the customer has corporate membership
# 5. Check if the customer has family membership
# 6. Calculate the total ticket price
# 7. Display the total ticket price
# 8. Stop

# ======================================================================================

# Basic Level Solution

# Define ticket prices
child_price = 7.50
adult_price = 10.00

# Input day of the week
day = int(input("Enter day (1-7 where 1 means Monday etc.): "))

# Check if the day is valid
if day < 1 or day > 7:
    print("Invalid day!")
else:
    # Input number of child and adult tickets
    child_tickets = int(input("No. of Child Tickets: "))
    adult_tickets = int(input("No. of Adult Tickets: "))

    # Check if the customer has corporate membership
    membership = input("Enter Membership (C)orporate/(N)o: ")

    # Calculate the total ticket price
    if 1 <= day <= 5:  # Weekday
        if membership.lower() == "c":
            total_price = (child_tickets * child_price + adult_tickets * adult_price) * 0.8  # Apply 20% discount
        else:
            total_price = child_tickets * child_price + adult_tickets * adult_price
    else:  # Weekend
        total_price = 10 * (child_tickets + adult_tickets)  # Fixed price at weekends

    # Display the total ticket price
    print(f"Please pay ${total_price:.2f}.")

# ======================================================================================

# What I did in class

# Ask for day
Day = int(input("Enter day: "))

# For Day variable
if Day < 1 or Day > 7:
    # Invalid day
    print("Incorrect day!")
else:
    Child = int(input("Enter number of child ticket: "))
    Adult = int(input("Enter number of adult ticket: "))
    Membership = str(input("Enter Membership (C)orporate/(F)amily/(N)o: "))

    if Day >= 1 and Day <= 5:
        # For weekday
        # Corporate
        if Membership in ['C','c']:
            total = ((Child * 7.50) + (Adult * 10)) * .8
            print(f"Please pay: $ {total:.2f}")
        # Family
        elif Membership in ['F','f']:
            total = (Child * 0) + (Adult * 10)
            print(f"Please pay: $ {total:.2f}")
        # No Membership
        else:
            total = (Child * 7.50) + (Adult * 10)
            print(f"Please pay: $ {total:.2f}")
    else:
        # For weekends, fixed price at $10
        total = (Child + Adult) * 10
        print(f"Please pay: $ {total:.2f}")

# ======================================================================================