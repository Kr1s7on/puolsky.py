# Author: Kriston Jomari
# Admin No: 231165R

score_list = []

for i in range(4):
    while True:
        score = int(input(f"Enter the score for subject {i+1}: "))

        if 0 <= score <= 100:
            score_list.append(score)
            break
        else:
            print("A score must be betwwen a range of 0 and 100!")

score_list.sort(reverse=True)
print(f"Score list in descending order is: {score_list}")