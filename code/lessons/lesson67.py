class test():
    def __init__(self,value):
        self.__x=value

    @property
    def x(self):
        print("x called")
        return self.__x

    @x.setter
    def x(self,x):
        if x<101:
            self.__x=x
            print(f'x value is: {self.x}')
        else:
            print(f'bad value..x value is {self.x}')

t1=test(123)
print(t1.x)
t1.x=34

t2=test(10)
t2.x=1000