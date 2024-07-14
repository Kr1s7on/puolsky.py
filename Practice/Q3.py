# Author: Kriston Jomari
# Admin No: 231165R

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Example input
text = "Hello World"
print(count_vowels(text))  # Output: 3
