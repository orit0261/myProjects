# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple

print(a)      # 3
print(b)      # 4.6
print(c)      # dog

my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))  # <class 'tuple'>

# Parentheses is optional
my_tuple = "hello",
print(type(my_tuple))  # <class 'tuple'>

my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3

# In operation
print('a' in my_tuple)
print('b' in my_tuple)

# Not in operation
print('g' not in my_tuple)

for item in my_tuple:
    print(item)

l =('a', 'p', 'p', 'l', 'e',),('g', 'r', 'e', 'e', 'n',)
for t in l:
  for e in t:
    print(":",e)

width = max(len(e) for t in l for e in t[:-1]) + 1
format=('%%-%ds' % width) * len(l[0])
print('\n'.join(format % tuple(t) for t in l))


# using list comprehension to get names
# using map() + itergetter() to get names
from operator import itemgetter
res = list(map(itemgetter(1), l))
print(res)
print ("List with only nth tuple element (i.e names) : " + str(res))

