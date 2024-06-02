# E Practical Q7
# Write python codes to compute the area & perimeter of rectangle given the width
# and height of the rectangle
# Input: width (in m) and height (in m) of a rectangle
# Process: Calculate the area & Perimeter of the rectangle
# Output: Display the area & perimeter of rectangle.

# Flowchart
# 1. Start
# 2. Input width and height
# 3. Calculate area and perimeter
# 4. Display the results
# 5. Stop

# ======================================================================================

# Basic Level Solution

# Input width and height from user
width = float(input("Enter width of the rectangle in meters: "))
height = float(input("Enter height of the rectangle in meters: "))

# Calculate area and perimeter
area = width * height
perimeter = 2 * (width + height)

# Display the results
print(f"The area of the rectangle is {area} square meters.")
print(f"The perimeter of the rectangle is {perimeter} meters.")

# ======================================================================================

# Advanced Level Solution

# # Input width and height from user
# while True:
#     try:
#         width = float(input("Enter width of the rectangle in meters: "))
#         if width <= 0:
#             print("Width must be a positive number. Please try again.")
#             continue
#         break
#     except ValueError:
#         print("Invalid input. Please enter a number.")

# while True:
#     try:
#         height = float(input("Enter height of the rectangle in meters: "))
#         if height <= 0:
#             print("Height must be a positive number. Please try again.")
#             continue
#         break
#     except ValueError:
#         print("Invalid input. Please enter a number.")

# # Calculate area and perimeter
# area = width * height
# perimeter = 2 * (width + height)

# # Display the results
# print(f"The area of the rectangle is {area} square meters.")
# print(f"The perimeter of the rectangle is {perimeter} meters.")