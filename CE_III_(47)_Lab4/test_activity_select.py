import unittest
import iterative_activity_select
import recursive_activity_select

class ActivityTestCase(unittest.TestCase):
    
    def testcase(self):
        self.assertListEqual(iterative_activity_select.activity_selector([1,5,6,7,4,8],[2,8,5,3,6,7]),[0,1,5])           
        self.assertListEqual(recursive_activity_select.activity_selector([1,5,6,7,4,8],[2,8,5,3,6,7],-1,6),[0,1,5])

if __name__ == '__main__':
    unittest.main()
