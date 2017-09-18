import multiprocessing
from time import ctime, sleep

count = 0

q = multiprocessing.JoinableQueue(1000)

def number(n=0):
    while n < 10:        
        yield n
        n += 1
    return n

def getl(q):
    print("In put_func",ctime())
    while True:
        sleep(0.5)
        item = q.get()
        print("pull",itme, 'out from q')
        count += item
        print("pull number count:", count)
        q.task_done()
        

def putl(number, q):
    n = number()
    while True:
        num = next(n)
        q.put(num)
        print("put", num, "into q")

        if num == 9:
            break


putl(number,q)



gets = []

n1 = multiprocessing.Process(target=getl, args=(q,))

n1.start()
n2 = multiprocessing.Process(target=getl, args=(q,))

n2.start()
q.join()
print("It's over!")


    
    

    

















    
    

