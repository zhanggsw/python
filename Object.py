class A(object):
    def met(self):
        print 'A.met'
        
class B(A):
    def met(self):
        print 'B.met'
#         A.met(self)
        super(B, self).met()
        
class C(A):
    def met(self):
        print 'C.met'
#         A.met(self)
        super(C, self).met()
        
class D(B,C):
    def met(self):
        print 'D.met'
#         B.met(self)
#         C.met(self)
        super(D, self).met()
       


if __name__ == '__main__':
    b = B()
    b.met()
    print "-----------"
    d = D()
    d.met()