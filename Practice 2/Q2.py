# Author: Kriston Jomari
# Admin No: 231165R

"""
Program to split bills with friends.

Input Name and Price.

Display:
    - Purchased Items
    - Total amt + 10%
    - Number of friends
    - Amt to be paid per person
"""

purchased_items = []
total = 0


def calc():
    global total
    item_purchased = input("Enter the name of the purchased item: ")
    purchased_items.append(item_purchased)
    price = float(input("The price: $"))
    total += price
    return


def end_prs():
    global total
    pax = int(input("\nPlease enter the number of pax to share the amount: "))
    final = total + (total * 0.10)
    shared = final / pax
    print(f"\nPurchased items: {purchased_items}")
    print(f"Total amount spent (including 10% additions for transportation): ${final:.2f}")
    print(f"Each friend to pay: ${shared:.2f}")
    return


def main():
    print("==== Contribution Calculator ====")

    while True:
        print("\nEnter 1 to add the name of purchased item")
        print("Enter 0 to add the name of purchased item")
        choice = int(input("Please select: "))

        if choice == 1:
            calc()

        elif choice == 0:
            end_prs()
            break

        else:
            print("Invalid choice")


main()
