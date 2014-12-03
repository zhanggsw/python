import unittest

class MyUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print 'setupclass'
        
    @classmethod
    def tearDownClass(self):
        print 'teardownclass'
        
    def setUp(self):
        print 'setup'
#     
    def tearDown(self):
        print 'teardown'
        
class MyTestList(MyUnitTest):
    @classmethod
    def setUpClass(self):
        super(MyTestList, self).setUpClass()
#
    @classmethod
    def tearDownClass(self):
        super(MyTestList, self).tearDownClass() 
           
    def setUp(self):
        super(MyTestList, self).setUp()

    def test_1(self):
        print 'test1'
        self.addCleanup(self.clear2(), self.clear1())
        
    def test_2(self):
        print 'test2'
        self.addCleanup(self.clear2())
        
    def clear1(self):
        print 'clear1'

    def clear2(self):
        print 'clear2'
        
class MyTestList2(MyUnitTest):
    
    @classmethod
    def setUpClass(self):
        super(MyTestList2, self).setUpClass()
        
    def setUp(self):
        super(MyTestList2, self).setUp()

    def test_3(self):
        print 'test3'
        self.addCleanup(self.clear3())
        
    def test_4(self):
        print 'test4'
        self.addCleanup(self.clear4())
        
    def clear3(self):
        print 'clear3'
    
    def clear4(self):
        print 'clear4'

if __name__ == '__main__':
    unittest.main()
    