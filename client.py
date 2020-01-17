# -*- coding: utf8 -*-

# Echo client program
import socket
import time
import threading

HOST = '0.0.0.0'    # The remote host
#PORT = 50007              # The same port as used by the server
PORT = 9000

def connect(name):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall('%s: Hello, world'%name)
    data = s.recv(1024)
    res = ' Received: '+ repr(data)
    print res
    #print name, ' Received', repr(data)
    s.close()
    time.sleep(15)


for i in range(50):
    if i % 10 == 0:
        time.sleep(5)
    name = 'cli_%s'%str(i)
    w = threading.Thread(target=connect, args=(name, ))
    w.start()

#for i in range(3):
#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    s.connect((HOST, PORT))
#    s.sendall('Hello, world')
#    data = s.recv(1024)
#    #s.close()
#    time.sleep(0.1)
#    print i, ' Received', repr(data)


