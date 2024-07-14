#Author: Wong Wen Bing
#Admin No: 230436M
results=[]
subj1=[]
while True:
    score=int(input("Enter the score for subject "+": "))
    if score<0:
        print("A score must be between a range of 0 and 100!")
    else: 
        results.append(score)
    
print("Score list in descending order is: ")
