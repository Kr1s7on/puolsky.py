# Author: Kriston Jomari
# Admin No: 231165R

def merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

# Example input
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
print(merge_dictionaries(dict1, dict2))  # Output: {'a': 1, 'b': 4, 'c': 5, 'd': 6}
