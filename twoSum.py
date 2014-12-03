from __future__ import division
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        half=target/2
        newNum=[]
        for i in num:
            newNum.append(abs(half-i))
        l=0
        result=[]   
        for i in newNum:
            l=l+1
            if newNum.count(i)==2:
                result.append(l)
        return tuple(result)
    
  
    def twoSum3(self, num, target):
        tmp_num = {}  
        for i in range(len(num)):  
            if target - num[i] in tmp_num:
                print "find" + str(tmp_num)  
                # here do not need to deal with the condition i = target-i  
                return (tmp_num[target-num[i]]+1, i+1)  
            else:  
                tmp_num[num[i]] = i
                print "else" + str(tmp_num)  
        return (-1, -1)         
  
if __name__ == '__main__':
    s=Solution()
    num=[2,3,5,7]
    print s.twoSum3(num,8)