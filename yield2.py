# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)




# Using for loop
for item in my_gen():
    print(item)


a = my_gen()
# We can iterate through the items using next().
print(next(a))
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and theirs states are remembered between successive calls.
print(next(a))

print(next(a))

# Finally, when the function terminates, StopIteration is raised automatically on further calls.
print(next(a))

print(next(a))



