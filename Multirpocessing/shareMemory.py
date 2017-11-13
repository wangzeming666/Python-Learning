import multiprocessing

class FloatChannel(object):
    def __init__(self, maxsize):
        self.buffer = multiprocessing.RawArray('d', 
            maxsize)
        self.buffer_len = multiprocessing.Value('i')
        self.empty = multiprocessing.Semaphore(1)
        self.full = multiprocessing.Semaphore(0)


    def send(self, values):
        self.empty.acquire()
        nitems = len(values)
        self.buffer_len = nitems
        self.buffer[:nitems] = values
        self.empty.release()
        #print("send")

    def recv(self):
        #self.full.acquire()
        print(self.buffer_len.value)
        values = self.buffer[:self.buffer_len.value]
        print("recv ")
        #self.full.release()
        return values

def consumer_test(count, ch):
    for i in range(count):
        values = ch.recv()

def producer_test(count, values, ch):
    for i in range(count):
        ch.send(values)

if __name__ == '__main__':
    ch = FloatChannel(10000)
    p = multiprocessing.Process(target=consumer_test,
        args=(1000, ch))
    p.start()

    values = [float(x) for x in range(1000)]
    producer_test(1000, values, ch)
    print("Done")
    p.join()



