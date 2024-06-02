# Loan Qualifier (ver 1) - using nested if-else
salary = int(input("Enter your annual salary : "))
years = int(input("Enter your years of service : "))
if salary < 30000:
    print ("you must earn at least 30000 to qualify")
else:
    if years < 2:
        print ("you must be on current job for at least 2 years to qualify")
    else:
        print ("you qualify for the loan")


# Loan Qualifier (ver 1.1) - using nested if-else
salary = int(input("Enter your annual salary : "))
years = int(input("Enter your years of service : "))
if salary >= 30000 :
    if years >= 2 :
        print("you qualify for the loan")
    else :
        print("you must be on current job for at least 2 years to qualify")
else :
    print("you must earn at least 30000 to qualify")


# Loan Qualifier (ver 2) - using "and" logical operator
salary = int(input("Enter your annual salary : "))
years = int(input("Enter your years of service : "))
if salary >= 30000 and years >= 2 :
    print("you qualify for the loan")
else :
    print("you do not qualify for the loan")


# Loan Qualifier (ver 2.1) - using "or" logical operator
salary = int(input("Enter your annual salary : "))
years = int(input("Enter your years of service : "))
if salary < 30000 or years < 2 :
    print("you do not qualify for the loan")
else :
    print("you qualify for the loan")

   
# Loan Qualifier (ver 3) - using if-elif-else
salary = int(input("Enter your annual salary : "))
years = int(input("Enter your years of service : "))
if salary < 30000 :
    print("you must earn at least 30000 to qualify")
elif years < 2 :
    print("you must be on current job for at least 2 years to qualify")
else :
    print("you qualify for the loan")