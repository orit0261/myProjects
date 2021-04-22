class test():
    def __init__(self,val):
        self.x = val

    @property
    def x(self):
        print('x called!')
        return self.__x

    @x.setter
    def x(self,x):
        if x<101:
            print('before..')
            self.__x = x
            print(f'x value is {self.x}')
        else:
            print(f'bad value..x is {self.x}')


t=test(10)
t.x
t.x=900