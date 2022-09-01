import socket

s = socket.socket()
print('socket Created')

s.bind(('localhost',9999))
# 3 connection listener
s.listen(3)
print("Waiting for connections")

while True:
    c , addr = s.accept()
    name = c.recv(1024).decode()

    print("Connect with",addr,name)
    c.send(bytes('Welocme to Telusko','utf-8'))

    c.close()