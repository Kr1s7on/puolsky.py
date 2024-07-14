# Author: Kriston Jomari
# Admin No: 231165R

employee_dict = {'Jimmy': 25.00, 'Tom': 48.50, 'Alice': 6.00}

meal_dict = {
    'BBM': [7.10, 'Big Breakfast Meal'],
    'TBE': [9.90, 'Turkey Bacon with Egg'],
    'MSO': [7.50, 'Mushroom Swiss Omelette'],
    'NLC': [6.60, 'Nasi Lemak with Chicken'],
    'CBV': [11.90, 'Curry Beef with Vegetable']
}

purchase_list = []


def purchase_meal(employee_name):
    """
    This function allows an employee to purchase meals from the company canteen
    using their pre-paid card balance.
    """
    if employee_name not in employee_dict:
        print("Invalid employee name.")
        return

    balance = employee_dict[employee_name]
    print(f"You have the balance of ${balance:.2f}")

    while True:
        purchase_choice = input("Would you like to purchase a meal? (Y/N): ").upper()
        if purchase_choice not in ("Y", "N"):
            print("Invalid input. Please enter Y or N.")
            continue

        if purchase_choice == "N":
            break

        meal_code = input("Enter meal code: ").upper()
        if meal_code not in meal_dict:
            print("Meal code is invalid!")
            continue

        meal_price = meal_dict[meal_code][0]
        if meal_price > balance:
            print(f"Big Breakfast Meal purchase unsuccessful, insufficient balance for purchasing.")
            print(f"You have the balance of ${balance:.2f}")
            continue

        # Successful purchase
        balance -= meal_price
        employee_dict[employee_name] = balance
        purchase_list.append(meal_dict[meal_code][1])
        print(f"{meal_dict[meal_code][1]} redeem successful")
        print(f"You have the balance of ${balance:.2f}")

    # Test code
    purchase_meal('Mary')
    purchase_meal('Jimmy')
    purchase_meal('Alice')

    if purchase_list:
        print("Meals purchased:", ", ".join(purchase_list))
    else:
        print("Meals purchased: NULL")
