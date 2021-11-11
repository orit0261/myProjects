

def get_input():
    data_lst = []
    for _ in range(4):
        data_lst.append(input())
    return data_lst

def set_data(*args):
    for arg in args:
        if str(arg).isdigit():
            print(arg)

data1 = get_input()
set_data(*data1)
