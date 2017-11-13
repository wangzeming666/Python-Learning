from multiprocessing import Queue
from multiprocessing import Process

def consumer(input):
    while True:
        item = input.get()
        if item is None:
            break
        print(item)
    print("Consumer done")

def producer(sequence, out_put):
    for item in sequence:
        out_put.put(item)

if __name__ == '__main__':
    q = Queue()
    cons_p = Process(target=consumer, 
        args=(q,))
    #cons_p.daemon = True
    cons_p.start()

    # Produce the sequence
    sequence = [1,2,3,4,5,6,7,8,9,10]
    producer(sequence, q)
    q.put(None)
    #cons_p.join()

