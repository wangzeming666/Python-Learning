from atexit import register
from random import randrange
from threading import Thread, Lock, current_thread
from time import sleep, ctime

class CleanOutPutSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3,7)))
remaining = CleanOutPutSet()

def loop(nsec):
    
    myname = current_thread().name
    with lock:
        
        remaining.add(myname)
        print('\n[%s] Started %s' % (ctime(), myname))
    
    sleep(nsec)
    with lock:
        remaining.remove(myname)
        print('\n[%s] Completed %s (%d secs)' %(ctime(), myname, nsec))
        print('\n    (remaining: %s)' % (remaining or 'NONE'))
    

def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()
        




_main()                     
