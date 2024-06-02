# Exercise 1 - FlourSales
# 1. iBake charges the following rates for their sales in their flour.
# 2. Draw the flow chart to show the logic flow.
# 3. Write a program that asks the user to enter the amount they would like to purchase in kg and
# then displays the price.
# Weight Rate per kg
# Over 100kg $2.80
# Over 40kg but not more than 100kg $3.00
# Over 20kg but not more than 40kg $3.20
# 20kg or less $3.60

# Flowchart
# 1. Start
# 2. Input amount of flour in kg
# 3. Check if the amount is over 100kg
# 4. Display the price
# 5. Stop

# ======================================================================================

# Basic Level Solution

# Input amount of flour from user
amount = float(input("Enter the amount of flour you would like to purchase in kg: "))

# Check if the amount is valid
if amount <= 0:
    print("Invalid amount. Please enter a number greater than 0.")
else:
    # Check the rate
    if amount > 100:
        rate = 2.80
    elif amount > 40:
        rate = 3.00
    elif amount > 20:
        rate = 3.20
    else:
        rate = 3.60

    # Calculate the price
    price = amount * rate

    # Display the price
    print(f"The price is ${price:.2f}.")

# ======================================================================================

# What I did in class

# Get the amount of flour from the user
flour = float(input("Please enter the amount of flour you want to purchase in kg: "))
if flour <= 0:
    print("Invalid amount entered.")
elif flour > 100:
    flour = flour * 2.8
elif flour > 40:
    flour = flour * 3
elif flour > 20:
    flour = flour * 3.2
else:
    flour = flour * 3.6
print(f"Amount payable: $ {flour:.2f}")

# ======================================================================================