str1 = input("get string:")
# if list(str1) == list(reversed(str1)):
if str1 == str1[::-1]:
    print("palindron found!")
else:
    print("no palindron found!")

import random

numbers = list(range(1, 10))

# we will read the line containing the numbers
guess = input("enter 6 different numbers from 1-37:")
# split it into a list of strings of these numbers
guess = guess.split()
# convert the string into integers
guess = [int(n) for n in guess]
# for the sake of bervity we didn't test the list for errors (not numbers, repeasting numbers not 6 exactly)
guess.sort()

result = random.sample(numbers, 3)
result.sort()

print("result:", result)

if result == guess:
    print("You Win")
else:
    print("You Lose")
