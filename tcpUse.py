from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZ = 4096
ADDR = (HOST, PORT)

tcpManySock = socket(AF_INET, SOCK_STREAM)
tcpManySock.connect(ADDR)

name = input('My usename:')
while True:
    data = input('> ')
    if data:
        tcpManySock.send(('[%s][%s] %s' %(ctime(),name,data)).encode('utf-8'))
