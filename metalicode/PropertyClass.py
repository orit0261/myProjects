class test():
    # test 1
    def __init__(self,val):
        self.x = val

    def __format__(self,x):
        return f'this is x:{x}'

    @property
    def x(self):
        print('x called!')
        return self.__x

    ' test 2'
    @x.setter
    def x(self,x):
        if x<101:
            print('before..')
            self.__x = x
            print('after..')
            print(f'x value is {self.x}')
            print('finish')
        else:
            print(f'bad value..x is {self.x}')


t=test(10)
print(f'{t}')
#t=test(900)
t.x
t.x=900