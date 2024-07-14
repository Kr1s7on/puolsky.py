# Author: Kriston Jomari
# Admin No: 231165R

score_list = []

subject_dict = {
  "UX Design": 80,
  "Programming": 70,
  "Data Modelling": 80,
  "Network Administration": 60
}

# Find highest scores
highest_score = max(subject_dict.values())

# Find the subjects of those high scores
highest_subjects = [subject for subject, score in subject_dict.items() if score == highest_score]

# Sort
highest_subjects.sort()

print(f"Subjects with highest score {highest_subjects}")
