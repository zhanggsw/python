'''
Created on

@author: zhangg
'''
def kthSmallestS1(l1,k):
# O(n) as sort() is O(n)
    l1.sort()   
    return l1[k-1]
    
print(kthSmallestS1([1,3,2,5], 2))
    