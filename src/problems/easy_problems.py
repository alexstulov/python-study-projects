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
    def correspondingBrackets(self, bracketsLine):
        bracketsDictionary = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        openBrackets = []
        for bracket in bracketsLine:
            if bracket in bracketsDictionary.keys():
                openBrackets.append(bracket)
                continue
            if len(openBrackets) > 0 and bracketsDictionary[openBrackets[-1]] == bracket:
                openBrackets.pop()
                continue
            return False
            
        return not len(openBrackets)
    def removeElement(self, nums, val):
        # in-place algorithm approach
        while val in nums: nums.remove(val)
        return len(nums)
    def findSubstring(self, haystack, needle):
        # let's imitate haystack.find(needle)
        i = 0
        needleSize = len(needle)
        haystackSize = len(haystack)
        while i+needleSize <= haystackSize:
            if haystack[i:i+needleSize] == needle:
                return i
            i+=1
        return -1
    def lengthOfLastWord(self, phrase):
        # phrase = phrase.split()
        # if phrase:
        #     return len(phrase[-1])
        phraseLength = len(phrase)
        start = 0
        end = 0
        for i in range(phraseLength):
            if phrase[i] == ' ' and i+1 < phraseLength and phrase[i+1] != ' ':
                start=i+1
            elif phrase[i] != ' ' and (i+1 == phraseLength or (i+1 < phraseLength and phrase[i+1] == ' ')):
                end = i
        return end - start + 1
    def searchInsertPosition(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left+right) // 2
            potentialMatch = nums[middle]
            if target == potentialMatch:
                return middle
            elif target < potentialMatch:
                right = middle - 1
            else:
                left = middle + 1
        while middle > 0 and nums[middle] > target:
            middle-=1
        while middle < len(nums) and nums[middle] < target:
            middle+=1
        return middle
    def plusOne(self, digits):
        # return list(map(int, list(str(int(''.join(map(str, digits)))+1)))) - easier, but less effective
        addition = 1
        for i in reversed(range(len(digits))):
            newDigit = digits[i]+addition
            if newDigit == 10:
                digits[i] = 0
            else:
                digits[i] = newDigit
                addition = 0
        if addition:
            digits = [addition]+digits
        return digits
