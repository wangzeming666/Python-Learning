import os
class hello:
    def fork(arg):
        print(arg)
        def p():
            print('hello')
        return p
        p()
        os.fork()
        os.fork()
        os.fork()
h = hello()
p = h.fork()
