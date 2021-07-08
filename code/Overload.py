class test:

    def __init__(self):
        print('init')

    def func1(self,val1=None,val2=None):
        print(f'val1={val1},val2={val2}')


t = test()
t.func1(1)
t.func1(val2=3)
t.func1()