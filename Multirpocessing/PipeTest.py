from multiprocessing import Pipe
from multiprocessing import Process
from multiprocessing import Pool

def consumer(pipe):
    con1,con2=pipe
    con2.close()
    while True:
        try:
            item = con1.recv()
        except EOFError:
            break
        print(item)
    print("Consumer done")

def producer(sequence, input):
    for item in sequence:
        input.send(item)

if __name__ == '__main__':
    (con1, con2) = Pipe()
    cons_p = Process(target=consumer, 
        args=((con1,con2),))
    cons_p.start()

    con1.close()
    sequence = [1,2,3,4,5,6]
    producer(sequence, con2)
    con2.close()

    cons_p.join()

    q = Manger.Queue()
    pool = Pool(4)
    pool.apply(func=consumer,args=q)
