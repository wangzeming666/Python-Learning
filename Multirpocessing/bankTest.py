import time
import multiprocessing

def depoist(in_m):
    for i in range(100):
        time.sleep(0.01)
        in_m.value = in_m.value+1

def withdraw(out_m):
    for i in range(200):
        time.sleep(0.01)
        out_m.value = out_m.value-1

if __name__ == '__main__':
    money = multiprocessing.Value('i', 1000)
    d = multiprocessing.Process(target=depoist, 
        args=(money,))
    w = multiprocessing.Process(target=withdraw, 
        args=(money,))

    d.start()
    w.start()
    d.join()
    w.join()
    print(money.value)
