# Create a program to prompt user for information and
# display the information on screen.
# A sample run of the program is as shown. Use
# InfoDisplay as the program name.
# Draw the flow chart for this program and
# Next proceed to create the program.

# BMI formula:
# weight(kg) /(height(m) X height(m))

name = input("Enter your name: ")

adminNumber = input("Enter your admin number: ")

age = int(input("Enter your age: "))

gender = input("Male/Female: ")

weight = float(input("Enter your weight in kg: "))

height = float(input("Enter your height in meters: "))

bmi = weight / (height * weight)

print ("Hello, " + str(name) + " (" + str(adminNumber) + ")" + "!\n")
print ("You are a " + str(age) + " year old " + gender + ".\n")
print ("Your BMI is " + str(bmi) + ".")