import multiprocessing
from time import ctime, sleep


def consumer1(input_q,count = 0):
    print("Into consumer1:", ctime())
    while True:
        #处理项
        item = input_q.get()
        count += item
        #此处替换为有用的工作
        print("pull1", item, "out of q")
        print("Count:",count)
        #发出信号通知主进程任务完成
        sleep(1)
        input_q.task_done()
    

def consumer2(input_q，count = 0):
    print("Into consumer2:", ctime())
    while True:
        #处理项
        item = input_q.get()
        #此处替换为有用的工作
        print("pull2", item, "out of q")
        #发出信号通知主进程任务完成
        sleep(1)
        input_q.task_done()


def producer(sequence, output_q):
    '''producer: 消费者；sequence:顺序'''
    print("Into proceduer:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("Out of producer:", ctime())

def number(n=1):
    while n < 1001:
        yield n
        n += 1

if __name__ == '__main__':
    
    q = multiprocessing.JoinableQueue()

    sequence = number()
    '''把sequence内的元素用生成器生产'''

    producer(sequence, q)
    cons = []

    cons_p1 = multiprocessing.Process(
        target=consumer1, args=(q,)) 
    cons_p1.daemon = True
    cons.append(cons_p1)


    cons_p2 = multiprocessing.Process(
        target=consumer2, args=(q,))
    cons_p2.daemon = True
    cons.append(cons_p2)

    for i in range(len(cons)):
        cons[i].start()



    q.join()

    print("all done!")
