from time import sleep, ctime
from myThread import MyThread

def fib(x):
    sleep(0.005)
    if x < 2:return 1
    return ((fib(x-2)+fib(x-1)))

def fac(x):
    sleep(0.1)
    if x < 2:return
    return (x * fac(x-1))

def sum(x):
    sleep(0.1)
    if x < 2: return 2
    return (x + sum(x-1))

funcs = [fib, fac, sum]
n = 12

def main():
    nfuncs = range(len(func))

    print('*** SINGLE THREAD'
