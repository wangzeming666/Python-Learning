# OS Manage Process 
import random
from queue import PriorityQueue

class Item(object):
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __lt__(self, other):
        return self.level < other.level

    def __repr__(self):
        return str(self.name) + ':' \
        +str(self.level)

if __name__ == '__main__':
    q = PriorityQueue()
    q.put(Item("Watch TV", 
          random.randint(1,20)))
    q.put(Item("Listen to music", 
          random.randint(1,20)))
    q.put(Item("Print Doc", 4))
    q.put(Item("Write Doc", 4))
    
    while not q.empty():
        print(q.get())

        