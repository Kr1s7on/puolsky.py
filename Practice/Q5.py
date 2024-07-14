# Author: Kriston Jomari
# Admin No: 231165R

def fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example input
num = int(input("Enter a number: "))
print(fibonacci_sequence(num))
