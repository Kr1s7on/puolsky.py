#Author: Wong Wen Bing
#Admin No: 230436M
purchases = {}

#find purchases and cost, add to the dictionary

print("="*4+"Contribution calculator"+"="*4)
while True:
    print("\nEnter 1 to add the name of purchased item \nEnter 0 to end the input of purchased item")
    choice=int(input("Please select: "))
    if choice==1:
        purchase_item=input("Enter the name of the purchased birthday itemz: ")
        price=input("The price: $")
        purchases.update({purchase_item: int(price)})
    else:
        break
print(purchases.values())
cost1=str(purchases.values()) #integer the value first, i dont udnerstand this part

total_cost=sum(cost1)*1.1
#cant work but before code can work
#there is no issue with the below code. 

pax_sharing=input("Please enter the number of pax to share the amount: ")
cost_perfriend=round(total_cost/pax_sharing,2)
print("Purchased items: "+ purchases)
print("Total amount spent (including 10% additions for transportation.):$" + total_cost)
print("Each friend to pay:$"+cost_perfriend)