'''
Created on 201477

@author: zhangg
'''
class Queue:
    def __init__(self):
        self.items = []
 
    def isEmpty(self):
        return self.items == []
 
    def enqueue(self, item):
        self.items.insert(0,item)
 
    def dequeue(self):
        return self.items.pop()
 
    def size(self):
        return len(self.items)


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
# one person leave if he has the potato in one round
        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

