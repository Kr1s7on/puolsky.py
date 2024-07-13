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

# Exercise 3B - BBTCashier
    # Update the program in Exercise 3A with this new promotion
        # • For customer that purchase, High Mountain Pouchong Tea with cream 
            # and coconut jelly, they will get 50% discount for their High Mountain Pouchong Tea and 30% for their coconut jelly.
        # • For customer whose order include any of these will get an discount of 10% for the total price
        # • Osmanthus Oolong Tea
        # • Green Lemon
        # • Grass Jelly

# Hint: use % and //

# ======================================================================================

# Prices for each category of the bubble tea components
tea_prices = [2, 3, 2, 4]
flavouring_prices = [0.8, 0.6, 1, 0]
topping_prices = [0.9, 1.1, 0.8, 0]

print("Please choose the various selection for your bubble tea.")

# Tea
print("\nType of tea:\n1. Green Tea\n2. Osmanthus Oolong Tea\n3. Black Tea\n4. High Mountain Pouchong Tea")

while True:
    tea = int(input("\nPlease pick the type of tea: ")) - 1  # minus 1 to match the list index (0-3)

    # Validation
    if 0 <= tea < 4:
        break  # Exit if valid
    print("Invalid input. Please enter a number between 1 and 4.")

# Flavouring
print("\n\nFlavouring:\n1. Honey\n2. Green Lemon\n3. Cream\n4. None")

while True:
    flavouring = int(input("\nPlease pick your flavouring: ")) - 1  # minus 1 to match the list index (0-3)

    # Validation
    if 0 <= flavouring < 4:
        break  # Exit if valid
    print("Invalid input. Please enter a number between 1 and 4.")

# Topping
print("\n\nToppings:\n1. Bubble\n2. Coconut Jelly\n3. Grass Jelly\n4. None")

while True:
    topping = int(input("\nPlease pick your topping: ")) - 1  # minus 1 to match the list index (0-3)

    # Validation
    if 0 <= topping < 4:
        break  # Exit if valid
    print("Invalid input. Please enter a number between 1 and 4.")

# Total payable = Tea + Flavouring + Topping
total_payable = tea_prices[tea] + flavouring_prices[flavouring] + topping_prices[topping]

# Apply promotions if conditions met
if tea == 3 and flavouring == 2 and topping == 1:

    # Apply a 50% discount on the tea and a 30% discount on the topping if Pouchong Tea, Cream flavouring, and Coconut Jelly topping
    total_payable -= tea_prices[3] * 0.5 + topping_prices[1] * 0.3

elif tea == 1 or flavouring == 1 or topping == 2:

    # If user chose Oolong Tea, Honey flavouring, or Grass Jelly topping, -> 10% discount
    total_payable *= 0.9

# Display the total payable
print(f"\n\nAmount payable: ${total_payable:.2f}")
