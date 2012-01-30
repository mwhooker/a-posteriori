import socket
import time
from Queue import Queue

q = Queue(1024)

#s = socket.create_connection(('localhost', 51234), 1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect(('127.0.0.1', 51234))
time.sleep(1)
s.send('hello, world')
print s.recv(4096)
s.close()
