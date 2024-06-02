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
# Samples output 1(User inputs are shown in bold)
# Please enter the amount of flour you want to purchase in kg: 0
# Invalid amount entered.
# Samples output 2(User inputs are shown in bold)
# Please enter the amount of flour you want to purchase in kg: 101
# Amount payable: $282.80
# Samples output 3(User inputs are shown in bold)
# Please enter the amount of flour you want to purchase in kg: 100
# Amount payable: $300.00
# Samples output 4(User inputs are shown in bold)
# Please enter the amount of flour you want to purchase in kg:41
# Amount payable: $123.00
# Samples output 5(User inputs are shown in bold)
# Please enter the amount of flour you want to purchase in kg: 40
# Amount payable: $128.00
# Samples output 6(User inputs are shown in bold)
# Please enter the amount of flour you want to purchase in kg: 21
# Amount payable: $67.20
# Samples output 5(User inputs are shown in bold)
# Please enter the amount of flour you want to purchase in kg: 20
# Amount payable: $72.00

# Get the amount of flour from the user
flour = float(input("Please enter the amount of flour you want to purchase in kg: "))
if flour <= 0:
    print("Invalid amount entered.")
elif flour > 100:
    print("Amount payable: $", flour * 2.80)
elif flour > 40:
    print("Amount payable: $", flour * 3.00)
elif flour > 20:
    print("Amount payable: $", flour * 3.20)
else:
    print("Amount payable: $", flour * 3.60)


