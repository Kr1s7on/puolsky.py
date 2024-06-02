# Exercise 3A - BBTCashier
# Write a program to calculate the total payable for the order of bubble tea.
# Customer can select various combination and the system will calculate the price to be
# displayed. Below are the list of selection available for the customers.
# Customer will select the type of tea, follow by flavouring and toppings.
# They can also choose not to select any flavouring and toppings.

# Hint: use % and //

# Tea Price
# Green Tea $2
# Osmanthus Oolong Tea $3
# Black Tea $2
# High Mountain Pouchong Tea $4
# Flavouring Price
# Honey $0.8
# Green Lemon $0.6
# Cream $1
# Topping Price
# Bubble $0.9
# Coconut Jelly $1.1
# Grass Kelly $0.8

# Flowchart
# 1. Start
# 2. Input type of tea
# 3. Input flavouring
# 4. Input topping
# 5. Calculate the total payable
# 6. Display the total payable
# 7. Stop

# ======================================================================================

# Basic Level Solution

# # Define prices
# tea_prices = {"Green Tea": 2, "Osmanthus Oolong Tea": 3, "Black Tea": 2, "High Mountain Pouchong Tea": 4}
# flavouring_prices = {"Honey": 0.8, "Green Lemon": 0.6, "Cream": 1}
# topping_prices = {"Bubble": 0.9, "Coconut Jelly": 1.1, "Grass Kelly": 0.8}

# # Input type of tea, flavouring, and topping
# tea = input("Enter type of tea: ")
# flavouring = input("Enter flavouring: ")
# topping = input("Enter topping: ")

# # Calculate the total payable
# total_payable = tea_prices.get(tea, 0) + flavouring_prices.get(flavouring, 0) + topping_prices.get(topping, 0)

# # Display the total payable
# print(f"The total payable is ${total_payable:.2f}")

# ======================================================================================

# Exercise 3B - BBTCashier
# Update the program in Exercise 3A with this new promotion
# • For customer that purchase, High Mountain Pouchong Tea with cream and coconut
# Jelly, they will get 50% discount for their High Mountain Pouchong Tea and 30% for
# their coconut jelly.
# • For customer whose order include any of these will get an discount of 10% for the
# total price
# • Osmanthus Oolong Tea
# • Green Lemon
# • Grass Jelly

# Hint: use % and //

# ======================================================================================

# What I did in class

# Define prices for each type of tea, flavouring, and topping
tea_prices = [2, 3, 2, 4]
flavouring_prices = [0.8, 0.6, 1, 0]
topping_prices = [0.9, 1.1, 0.8, 0]

# Display the menu for the user
print("Please choose the various selection for your bubble tea.\n")

# Ask the user to choose a type of tea
print("\nType of tea:\n1. Green Tea\n2. Osmanthus Oolong Tea\n3. Black Tea\n4. High Mountain Pouchong Tea")
while True:
    tea = int(input("\nPlease pick the type of tea: ")) - 1
    # Check if the user's input is valid (between 1 and 4)
    if 0 <= tea < 4:
        break
    print("Invalid input. Please enter a number between 1 and 4.")

# Ask the user to choose a flavouring
print("\n\nFlavouring:\n1. Honey\n2. Green Lemon\n3. Cream\n4. None")
while True:
    flavouring = int(input("\nPlease pick your flavouring: ")) - 1
    # Check if the user's input is valid (between 1 and 4)
    if 0 <= flavouring < 4:
        break
    print("Invalid input. Please enter a number between 1 and 4.")

# Ask the user to choose a topping
print("\n\nToppings:\n1. Bubble\n2. Coconut Jelly\n3. Grass Jelly\n4. None")
while True:
    topping = int(input("\nPlease pick your topping: ")) - 1
    # Check if the user's input is valid (between 1 and 4)
    if 0 <= topping < 4:
        break
    print("Invalid input. Please enter a number between 1 and 4.")

# Calculate the total payable by adding the prices of the chosen tea, flavouring, and topping
total_payable = tea_prices[tea] + flavouring_prices[flavouring] + topping_prices[topping]

# Apply promotions if the user's choices meet the conditions
if tea == 3 and flavouring == 2 and topping == 1:
    # If the user chose High Mountain Pouchong Tea, Cream flavouring, and Coconut Jelly topping, apply a 50% discount on the tea and a 30% discount on the topping
    total_payable -= tea_prices[3] * 0.5 + topping_prices[1] * 0.3
elif tea == 1 or flavouring == 1 or topping == 2:
    # If the user chose Osmanthus Oolong Tea, Honey flavouring, or Grass Jelly topping, apply a 10% discount on the total payable
    total_payable *= 0.9

# Display the total payable
print(f"\n\nAmount payable: ${total_payable:.2f}")

# ======================================================================================