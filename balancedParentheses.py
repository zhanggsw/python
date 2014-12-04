'''
Created on 2014623

@author: zhangg
'''
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
     
def balancedParenthese(str):
    s = Stack()
    balanced = True
    for c in str:
        if c == "(":
            s.push(c)
        if c == ")":
            if s.isEmpty() == True:
                balanced = False
                break
            else:
                s.pop()
    if s.isEmpty() == False:
        balanced = False
    return balanced

print balancedParenthese(")")


    
        
            
    
