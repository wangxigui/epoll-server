# -*- coding: utf8 -*-

import socket
import threading
from multiprocessing import Process

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

def workerProcess(name):
    while 1:
        try:
            conn, addr= s.accept()
            print name, 'accept! ', conn, addr
            while 1:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
        except (KeyboardInterrupt, SystemExit):
            return 0
        except Exception as x:
            logger.exception(x)


for i in range(2):
    worker_name = 'worker %s'%str(i)
    #w = threading.Thread(target=workerProcess, args=(worker_name,))
    w = Process(target=workerProcess, args=(worker_name,))
    #w.w.daemon = True
    w.start()
    print worker_name, 'is starting !'
