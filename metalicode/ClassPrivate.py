class myClass():
    def __init__(self):
        self.x = "public"
        self._x="proteced"
        self.__x="private"

    def print_x(self):
        print(self.__x)
c = myClass()
print(c.x)
print(c._x)
#print(c.__x) # private variable #AttributeError: 'myClass' object has no attribute '__x'
c.print_x()
print(c._myClass__x)# private variable
