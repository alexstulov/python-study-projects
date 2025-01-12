import unittest
from msa import MergeArrays

class TestMergeArraysMethods(unittest.TestCase):
    mergeArrays = MergeArrays()
    def testMergeSortedLists(self):
        self.assertEqual(self.mergeArrays.mergeSortedLists([1],1,[],0), [1])
        self.assertEqual(self.mergeArrays.mergeSortedLists([0],0,[1],1), [1])
        self.assertEqual(self.mergeArrays.mergeSortedLists([2,0],1,[1],1), [1,2])
        self.assertEqual(self.mergeArrays.mergeSortedLists([1,2,3,0,0,0],3,[2,5,6],3), [1,2,2,3,5,6])
        self.assertEqual(self.mergeArrays.mergeSortedLists([1,2,4,5,6,0],5,[3],1), [1,2,3,4,5,6])
        
    def testMerge(self):
        num1 = [1,2,3,0,0,0]
        self.mergeArrays.merge(num1, 3, [2,5,6], 3)
        self.assertEqual(num1, [1,2,2,3,5,6])
        
        num1 = [1]
        self.mergeArrays.merge(num1, 1, [], 0)
        self.assertEqual(num1, [1])
        
        num1 = [0]
        self.mergeArrays.merge(num1, 0, [1], 1)
        self.assertEqual(num1, [1])
        
if __name__ == '__main__':
    unittest.main()