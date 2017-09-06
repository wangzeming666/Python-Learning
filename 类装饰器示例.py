def class_deco(cls):
    print(1)
    class B:
        def pr(self):
            print(1)
    return B
		

@class_deco
class A:
    def pr(self):
        print(2)

a = A()
a.pr()
