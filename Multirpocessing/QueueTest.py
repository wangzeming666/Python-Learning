from multiprocessing import JoinableQueue
from multiprocessing import Process

def consumer(input):
    while True:
        item = input.get()
        print(item)
        input.task_done()

def producer(sequence, out_put):
    for item in sequence:
        out_put.put(item)

if __name__ == '__main__':
    q = JoinableQueue()
    cons_p = Process(target=consumer, 
        args=(q,))
    cons_p.daemon = True
    cons_p.start()
    
    sequence = [1,2,3,4]
    producer(sequence, q)
    q.join()

