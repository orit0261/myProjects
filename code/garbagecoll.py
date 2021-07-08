import sys

class myobj:
    pass

x = myobj()
y=x
z=y
#x = 5000
#y = 5000
print(x is y)
del y
print(sys.getrefcount(x))