# Author: Kriston Jomari
# Admin No: 231165R

"""
Write a function called calculate_grades that takes in a list of dictionaries
    where each dictionary represents
    a student's name and their marks for three subjects: Math, Science, and English.

The function should calculate
    the average marks for each student
    and return a new list of dictionaries
        where each dictionary contains
            the student's name
            and their average marks.
"""

def calculate_grades(students):
    result = []
    for student in students:
        name = student['name']
        avg = (student['Math'] + student['Science'] + student['English']) / 3
        result.append({'name': name, 'average': round(avg, 2)})
    return result

# Example input
students = [
    {'name': 'Alice', 'Math': 85, 'Science': 92, 'English': 78},
    {'name': 'Bob', 'Math': 75, 'Science': 88, 'English': 82},
    {'name': 'Charlie', 'Math': 90, 'Science': 85, 'English': 95}
]

print(calculate_grades(students))
