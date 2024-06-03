# ======================================================================================

# Author: Kriston Jomari
# Admin No: 231165R

# ======================================================================================

fish = 6.50
happy = 4.50

orders = int(input("Please enter the number of orders you wish to place: "))

counter = 0

while counter < orders:
    try:
        print("Please choose your main course: \n(1) Fish Burger \n(2) Happy Meal")
        course = int(input("Your selection please: "))

        if course == 1:
            total = fish

        else:
            print("Happy Meal comes with a gift: \n(1) Toy \n(2) Book")
            input("Your selection please: ")
            total = happy

        total += total
        counter += 1
    except ValueError:
        print("Invalid input.")

print(f"Total payable: ${total:.2f}")