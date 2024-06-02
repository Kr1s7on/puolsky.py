#  Week 7 Extra Practical


# ======================================================================================
# Task 1: Write a program to print "Hello World" using a while loop

# Initialize a counter variable
counter = 0

# While loop to print "Hello World" 5 times
while counter < 5:
    print("Hello World")
    # Increment the counter
    counter += 1

print("\n")  # Adding a newline for better separation of outputs
# ======================================================================================


# ======================================================================================
# Task 2: Write a program to print "Hello World" using a for loop

# For loop to print "Hello World" 5 times
for i in range(5):
    print("Hello World")

print("\n")  # Adding a newline for better separation of outputs
# ======================================================================================


# ======================================================================================
# Task 3: Using a while loop that reads 5 positive integer numbers, determine if it is even or odd,
# keep count of the number of even and odd numbers, and display the outcome.

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Initialize a counter to keep track of the number of inputs
input_counter = 0

# While loop to read 5 positive integers
while input_counter < 5:
    try:
        # Read input from the user
        number = int(input("Enter a positive integer: "))
        
        # Check if the number is positive
        if number <= 0:
            print("Please enter a positive integer.")
            continue
        
        # Determine if the number is even or odd
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
        # Increment the input counter
        input_counter += 1
    
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

# Display the count of even and odd numbers
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")

print("\n")  # Adding a newline for better separation of outputs
# ======================================================================================


# ======================================================================================
# Task 4: Rewrite the program (Task 3), using a for loop.

# Reset counters for even and odd numbers
even_count = 0
odd_count = 0

# For loop to read 5 positive integers
for _ in range(5):
    while True:
        try:
            # Read input from the user
            number = int(input("Enter a positive integer: "))
            
            # Check if the number is positive
            if number <= 0:
                print("Please enter a positive integer.")
                continue
            
            # Determine if the number is even or odd
            if number % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
            
            # Break the loop if input is valid
            break
        
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

# Display the count of even and odd numbers
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
# ======================================================================================