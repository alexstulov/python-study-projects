import unittest
from easy_problems import Solution

class TestStringMethods(unittest.TestCase):
    solution = Solution()
    def testMaxProductionDifference(self):
        self.assertEqual(self.solution.maxProductionDifference([5,6,2,7,4]), 34)
        self.assertEqual(self.solution.maxProductionDifference([4,2,5,9,7,4,8]), 64)
        self.assertEqual(self.solution.maxProductionDifference([]), 0)
        self.assertEqual(self.solution.maxProductionDifference([1,2]), 0)
        self.assertEqual(self.solution.maxProductionDifference([1,2,3]), 0)

    def testBuyChoco(self):
        self.assertEqual(self.solution.buyChoco([1,2,2], 3), 0)
        self.assertEqual(self.solution.buyChoco([3,2,3], 3), 3)
        
    def testTwoSum(self):
        self.assertEqual(self.solution.twoSum([2,7,11,15], 9), [0,1])
        self.assertEqual(self.solution.twoSum([3,2,4], 6), [1,2])
        self.assertEqual(self.solution.twoSum([0,0,0,3,0,0,0,4], 7), [3,7])

    def testMaxScore(self):
        self.assertEqual(self.solution.maxScore("011101"), 5)
        self.assertEqual(self.solution.maxScore("00111"), 5)
        self.assertEqual(self.solution.maxScore("1111"), 3)
        self.assertEqual(self.solution.maxScore("00"), 1)
        self.assertEqual(self.solution.maxScore("01"), 2)
        self.assertEqual(self.solution.maxScore("11"), 1)
        self.assertEqual(self.solution.maxScore("10"), 0)

    def testMinOperations(self):
        self.assertEqual(self.solution.minOperations("01001"), 2)
        self.assertEqual(self.solution.minOperations("0100"), 1)
        self.assertEqual(self.solution.minOperations("1111"), 2)
        self.assertEqual(self.solution.minOperations("000"), 1)
        self.assertEqual(self.solution.minOperations("10"), 0)
        self.assertEqual(self.solution.minOperations("0"), 0)
        
    def testIsPalindrome(self):
        self.assertEqual(self.solution.isPalindrome(121), True)
        self.assertEqual(self.solution.isPalindrome(-121), False)
        self.assertEqual(self.solution.isPalindrome(10), False)
        
    def testRomanToInt(self):
        self.assertEqual(self.solution.romanToInt('III'), 3)
        self.assertEqual(self.solution.romanToInt('LVIII'), 58)
        self.assertEqual(self.solution.romanToInt('MCMXCIV'), 1994)
        
    def testLongestCommonPrefix(self):
        self.assertEqual(self.solution.longestCommonPrefix(['flower','flow','flight']), 'fl')
        self.assertEqual(self.solution.longestCommonPrefix(['dog', 'racecar', 'car']), '')
        self.assertEqual(self.solution.longestCommonPrefix(['a']), 'a')
        
    def testCorrespondingBrackets(self):
        self.assertEqual(self.solution.correspondingBrackets("()"), True)
        self.assertEqual(self.solution.correspondingBrackets("()[]{}"), True)
        self.assertEqual(self.solution.correspondingBrackets("]"), False)
        self.assertEqual(self.solution.correspondingBrackets("("), False)
        self.assertEqual(self.solution.correspondingBrackets("(]"), False)
        self.assertEqual(self.solution.correspondingBrackets("((())]"), False)
        self.assertEqual(self.solution.correspondingBrackets("((([))"), False)

    def testRemoveElement(self):
        self.assertEqual(self.solution.removeElement([3,2,2,3], 3), 2)
        self.assertEqual(self.solution.removeElement([0,1,2,2,3,0,4,2], 2), 5)
    def testFindSubstring(self):
        self.assertEqual(self.solution.findSubstring("sadbutsad","sad"), 0)
        self.assertEqual(self.solution.findSubstring("saturdaysad","sad"), 8)
        self.assertEqual(self.solution.findSubstring("leetcode","leeto"),- 1)
    def testLengthOfLastWord(self):
        self.assertEqual(self.solution.lengthOfLastWord("i"), 1)
        self.assertEqual(self.solution.lengthOfLastWord("i "), 1)
        self.assertEqual(self.solution.lengthOfLastWord(" i"), 1)
        self.assertEqual(self.solution.lengthOfLastWord('Hello World'), 5)
        self.assertEqual(self.solution.lengthOfLastWord("   fly me   to   the moon  "), 4)
        self.assertEqual(self.solution.lengthOfLastWord("luffy is still joyboy"), 6)
if __name__ == '__main__':
    unittest.main()