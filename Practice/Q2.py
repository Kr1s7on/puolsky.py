# Author: Kriston Jomari
# Admin No: 231165R

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_even_numbers():
    even_list = []
    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

print(filter_even_numbers())
