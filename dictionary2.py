# Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item, return (key,value)
# Output: (5, 25)
print(squares.popitem())

# Output: {1: 1, 2: 4, 3: 9}
print(squares)

print(squares.popitem())
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
#print(squares)


# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)

for item in marks.values():
    print('val=',item)

for key in marks.keys():
     print('key=',key)

for k,v in marks.items():
     print('key=',k,"val=",v)

# Output: ['English', 'Math', 'Science']
print(list(sorted(marks.keys())))

# Dictionary Built-in Functions
squares = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# all()	Return True if all keys of the dictionary are True (or if the dictionary is empty).
# any()	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
# len()	Return the length (the number of items) in the dictionary.
# cmp()	Compares items of two dictionaries. (Not available in Python 3)
# sorted()	Return a new sorted list of keys in the dictionary.

# Output: False
print(all(squares))

# Output: True
print(any(squares))

# Output: 6
print(len(squares))

# Output: [0, 1, 3, 5, 7, 9]
print(sorted(squares))