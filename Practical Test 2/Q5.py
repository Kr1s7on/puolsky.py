#Author: Wong Wen Bing
#Admin No: 230436M


employee_dict = {'Jimmy': 25.00, 'Tom': 48.50, 'Alice': 6.00}

meal_dict =  {'BBM': [7.10, 'Big Breakfast Meal'],
              'TBE': [9.90, 'Turkey Bacon with Egg' ],
              'MSO': [7.50, 'Mushroom Swiss Omelette'],
              'NLC': [6.60, 'Nasi Lemak with Chicken'],
              'CBV': [11.90, 'Curry Beef with Vegetable']}
purchase_list=[]
#retrieve employee name
employeename=input("Enter employee name: ")

#apply function
def purchase_meal(employeename):
    if employeename not in employee_dict:
        print("Invalid employee Name.")
    else: 
        balance=employee_dict[employeename]
        #print balance
        print("You have the balance of $" + balance)
        #print option
        meal_option=input("Would you like to purchase meal(Y/N): ")
        if meal_option=='Y': 
            meal_code=input("Enter meal code: ")
            if meal_code not in meal_dict:
                print("meal code is invalid. ")
            else:
                cost=meal_dict[meal_code]
                final_balance=balance-cost
                if final_balance>0: 
                    #printing final balance
                    print(meal_code + "redeem successful")
                    print("Your balance is "+ balance)
                    employee_dict({[employeename]:balance})
                    #saving meals inside the other dict. 
                    purchase_list.append(meal_code)
                else: 
                    print("Purchase unsuccessful, insufficient balance for purchasing.")
                    print("Meals purchased: NULL")
            
purchase_meal(employeename)