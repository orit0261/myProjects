import os
import time
from multiprocessing import Process

def square(numbers):
    p_id=os.getpid()
    print("my id is:",p_id)
    for num in numbers:
        res = num * num
        time.sleep(0.5)
        print("the number {} square to {}".format(num,res))

def my_id(task_id):
    print("my id is:",task_id)

if __name__ == '__main__':
    numbers=range(8)
    lst_proc=[]
    for i in range(10):
      p = Process(target=square, args=(numbers,))
      lst_proc.append(p)
      p.start()
      p.join()