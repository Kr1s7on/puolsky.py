# ======================================================================================

# Author: Kriston Jomari
# Admin No: 231165R

# ======================================================================================

# Question 2 (25 points)
# You are tasked to develop a program for
# a restaurant to compute the total cost of meals for a customer.

# The buffet prices are shown below:
# Meal Type   Weekdays    Weekends
# Lunch       $41         $71
# Dinner      $52         $88

# Customers will enjoy discount when they pay by credit card.
#             Lunch   Dinner
# Discount    10 %    15 %

# Your program should use multiple 'and' operators to combine conditions to calculate the buffet price,
# for example, <condition A> and <condition B> and <condition C>

# Choose weekday or weekend Pass (weekday/weekend): weekday
# Enter your meal type (lunch/dinner): lunch
# Will you pay by credit card (Y/N): Y
# The buffet price for a discounted lunch on weekday is $36.9

# Choose weekday or weekend Pass (weekday/weekend): weekend
# Enter your meal type (lunch/dinner): dinner
# Will you pay by credit card (Y/N): N
# The buffet price for a dinner on weekend is $88

# ======================================================================================

# Define prices
lunch_day = 41
lunch_end = 71
dinner_day = 52
dinner_end = 88

# Input whether weekday/end
day = str(input("Choose weekday or weekend Pass (weekday/weekend): "))

if day != "weekday" and day != "weekend":
    print("Invalid day!")
else:
    # Input type of meal
    meal_type = str(input("Enter your meal type (lunch/dinner): "))
    # Credit card or not
    c_card = str(input("Will you pay by credit card (Y/N): "))

    # Calculate prices
    if day == "weekday":
        # Lunch weekday
        if c_card == "Y" and meal_type == "lunch":
            price = lunch_day * 0.9     # 10% discount ,CCard
        else:
            price = lunch_day

            # Dinner weekday
            if c_card == "Y" and meal_type == "dinner":
                price = dinner_day * 0.85     # 15% discount ,CCard
            else:
                price = dinner_day
    else:
        # Lunch weekend
        if c_card == "Y" and meal_type == "lunch":
            price = lunch_end * 0.9  # 10% discount ,CCard
        else:
            price = lunch_end

            # Dinner weekend
            if c_card == "Y" and meal_type == "dinner":
                price = dinner_end * 0.85  # 15% discount ,CCard
            else:
                price = dinner_end

    # Print output
    print(f"The buffet price for a {meal_type} on {day} is ${price:.2f}")