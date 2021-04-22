# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
import sys


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i

# Driver code to check above generator function
mygenerator = create_generator()  # create a generator
print(mygenerator)  # mygenerator is an object!
for i in mygenerator:
    print(i)

for value in simpleGeneratorFun():
    print(value)


# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    i = 1;

    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point


# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)
