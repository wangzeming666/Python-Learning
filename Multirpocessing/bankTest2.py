import time
import multiprocessing

def depoist(in_m,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        in_m.value = in_m.value+1
        lock.release()

def withdraw(out_m,lock):
    for i in range(200):
        time.sleep(0.01)
        lock.acquire()
        out_m.value = out_m.value-1
        lock.release()

if __name__ == '__main__':
    money = multiprocessing.Value('i', 1000)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=depoist, 
        args=(money,lock))
    w = multiprocessing.Process(target=withdraw, 
        args=(money,lock))

    d.start()
    w.start()
    d.join()
    w.join()
    print(money.value)
