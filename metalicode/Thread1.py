import threading


def worker(val):
    mydata = threading.local()
    mydata.x = 0
    print(mydata)
    for i in range(val):
        mydata.x += 1
    print(str(mydata.x), "-->", str(threading.currentThread()),'\t')
    print(str(threading.active_count()),'\t')


t1 = threading.Thread(name='Thread no.1', target=worker, args=(3,))
t1.start()
t2 = threading.Thread(name='Thread no.2', target=worker, args=(5,))
t2.start()
