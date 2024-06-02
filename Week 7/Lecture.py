# ======================================================================================

for i in "Python":
    print(i)

# ======================================================================================

for i in [1,2,3,4,5]:
    print(i)

# ======================================================================================

# first number x where you want to start then y is end (x,y,z) z is the increment
for i in range(1,11,2):
    print(i)

# ======================================================================================

# for loop
for i in range(10,0,-1):
    print(i)

# ======================================================================================

# Convert for loop to while loop
for i in range(1,6):
    print(i)

i = 1
while (i < 9): # while i <=5:
    print(i)
    i = i + 1

# ======================================================================================

# Define the secret number
secret_num = 7

guess_num = int(input("Guess the number: "))
while (guess_num != secret_num):
    guess_num = int(input("Guess the number: "))
print("Bingo! You got it!")

# ======================================================================================

# break out from a loop
num = 5
while True :
    guess = int(input('What is your guess? '))
    if (guess == num):
        break
    else:
        print('Try again!')
print('You hit the jackpot!')

# ======================================================================================