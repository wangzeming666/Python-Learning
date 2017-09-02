from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 4096
ADDR = (HOST, PORT)

tcpManySock = socket(AF_INET, SOCK_STREAM)
tcpManySock.bind(ADDR)
tcpManySock.listen(10)
tcpdict = []
while True:
    tcpManySock, addr = tcpManySock.accept()
    if [tcpManySock, addr] not in tcpdict:
        tcpdict.append([tcpManySock, addr])
    lenth = len(tcpdict)
    data = tcpManySock.recv(BUFSIZ)
    if data:
        print(data.decode('utf-8'))
        for i in range(lenth):
            tcpdict[i][0].send(('[%s] %s'%(ctime(), data)).encode('utf-8'))
