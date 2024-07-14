#Author: Wong Wen Bing
#Admin No: 230436M


inventory_info = {
           '1': {
               'Product Name': 'Apple',
               'prices': [1.2,1.5,1.3]},
           '2': {
               'Product Name': 'Banana',
               'prices': [0.8, 0.9, 0.7, 0.6, 0.6]},
           '3': {
               'Product Name': 'Orange',
               'prices': [1.0, 1.2, 0.9, 1.1]},
               }

def prod_info():
    print("Product information: "+len(inventory_info))
    #i want to get the value in the dictionary but im not really sure how
    print(inventory_info.keys{0}{'Product Name'})
    print("Maximum Price:" + max(inventory_info['1','2','3']+['prices']))
    #calculating average, in this case, will be hard coded abit
    average=sum(inventory_info['1']['prices'])/len(inventory_info['1']['prices'])
    print("Average Price: " + average)
    
prod_info()
#due to a lack of time, can only produce here    
    