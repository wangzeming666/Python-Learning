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
    lock.acquire()
    myname = current_thread().name
    
    remaining.add(myname)
    print('\n[%s] Started %s' % (ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('\n[%s] Completed %s (%d secs)' %(ctime(), myname, nsec))
    print('\n    (remaining: %s)' % (remaining or 'NONE'))
    lock.release()

def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()
        

@register
def _atexit():
    print ('all DONE at:', ctime())


_main()                                        




