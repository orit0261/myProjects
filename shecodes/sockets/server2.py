import socket
import time
import pickle

d = {1:"Hey", 2: "There"}
msg = pickle.dumps(d)
print(msg)

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Conection from {address} has been established!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADER_SIZE}}' + msg  # <10 print 10 spaces left align

    clientsocket.send(bytes(msg,'utf-8'))

    while True:
        time.sleep(3)
        msg = f"the time is:{time.time()}"
        msg = f'{len(msg):<{HEADER_SIZE}}' + msg  # <10 print 10 spaces left align
        clientsocket.send(bytes(msg,'utf-8'))

    #clientsocket.close()
