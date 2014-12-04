'''
Created on 2014623

@author: zhangg
'''
import string
class Stack():
    def __init__(self):
        self.item=[]
    def push(self,e):
        self.item.append(e)
    def pop(self):
        return self.item.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

s = Stack()
s.push("a")
s.push("b")
s.pop()

class Solution():
    def stringRev(self,oriStr):
        s = Stack()
        for e in oriStr:
            s.push(e)
        l=[]
        for i in range(len(oriStr)):
            l.append(s.pop())
        newStr=''.join(l)
        return newStr
        
        
s=Solution()
print s.stringRev("test")
         


    