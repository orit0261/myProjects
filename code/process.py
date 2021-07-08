import multiprocessing

def workers(x,y):
    print(f'{x}  {y}')

if __name__=='__main__':
    print(multiprocessing.cpu_count())
    with multiprocessing.Pool(5) as p:
        p.starmap(workers,[("a",1),("b",2)])