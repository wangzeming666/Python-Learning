import os
import time
from multiprocessing import Process

class Timer(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print("My thread pid is %d level is %d" 
             %(os.getpid(),
             os.getpriority(os.PRIO_PROCESS,
                os.getpid())))
        os.setpriority(os.PRIO_PROCESS,
                os.getpid(), 1)
        print("My thread level is now %d"
            %os.getpriority(os.PRIO_PROCESS,
                os.getpid()))

        while True:
            time.sleep(self.interval)
            print("Current time is %s"
                %time.ctime())

if __name__ == '__main__':
    t = Timer(20) 
    t.start()


 