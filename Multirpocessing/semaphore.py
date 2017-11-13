import multiprocessing
import time

def worker(s, i):
    s.acquire()
    print("current process %s get"
        %multiprocessing.current_process().name)
    time.sleep(i)
    s.release()
    print("current process %s release"
        %multiprocessing.current_process().name)

if __name__ == '__main__':
    s = multiprocessing.Semaphore(2)
    for i in range(5):
        p = multiprocessing.Process(target=worker,
            args=(s,i))
        p.start()
        p.join()


    print("Main End")   