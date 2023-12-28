def generateAdjacentStrings(length):
    alternatingString = ""
    for i in range(length+1):
        alternatingString += "0" if i % 2 else "1"
    return [alternatingString[1:], alternatingString[:len(alternatingString)-1]]

def countStringsDifference(str1, str2):
    return sum(1 for a, b in zip(str1, str2) if a != b)

class Solution:
    def maxProductionDifference(self, nums):
        nums.sort()
        nums_size = len(nums)
        if (nums_size < 4):
            return 0
        return nums[nums_size-1]*nums[nums_size-2]-nums[0]*nums[1]
    def buyChoco(self, prices, money):
        prices.sort()
        twoCheapestChocosPrices = prices[0] + prices[1]
        if (twoCheapestChocosPrices <= money):
            return money - twoCheapestChocosPrices
        return money
    def twoSum(self, nums, target):
        for firstI, first in enumerate(nums):
            try:
                index = nums.index(target-first, firstI+1)
            except:
                index = -1
            if index >= 0:
                return [firstI, index]
        return None
    def maxScore(self, binaryString):
        counterLeft = binaryString.count('0', 0, 1)
        counterRight = binaryString.count('1', 1)
        max = counterLeft + counterRight
        i=1
        while i < len(binaryString)-1:
            if (binaryString[i] == '0'):
                counterLeft += 1
            elif (binaryString[i] == '1'):
                counterRight -= 1
            sum = counterLeft + counterRight
            max = max if max > sum else sum
            i+=1
        return max
    def minOperations(self, binaryString):
        [oFirstString, iFirstString] = generateAdjacentStrings(len(binaryString))
        oFirstMaskDiff = countStringsDifference(binaryString, oFirstString)
        iFirstMaskDiff = countStringsDifference(binaryString, iFirstString)
        return min(oFirstMaskDiff, iFirstMaskDiff)
    def isPalindrome(self, number):
        return str(number) == str(number)[::-1]
    def romanToInt(self, romanNumber):
        vocabulary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        number = 0
        
        for i in range(len(romanNumber) - 1):
            if vocabulary[romanNumber[i]] < vocabulary[romanNumber[i+1]]:
                number -= vocabulary[romanNumber[i]]
            else:
                number += vocabulary[romanNumber[i]]
        return number + vocabulary[romanNumber[-1]]
    def longestCommonPrefix(self, words):
        words.sort()
        result = ''
        first = words[0]
        last = words[-1]
        for i in range(min(len(first),len(last))):
            if (first[i] != last[i]):
                return result
            result += first[i]
        return result