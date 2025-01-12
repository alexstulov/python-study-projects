from icecream import ic
from collections import Counter
import re
def generateAdjacentStrings(length):
    alternatingString = ""
    for i in range(length+1):
        alternatingString += "0" if i % 2 else "1"
    return [alternatingString[1:], alternatingString[:len(alternatingString)-1]]

def countStringsDifference(str1, str2):
    return sum(1 for a, b in zip(str1, str2) if a != b)

def maxProfitHelper(prices,thePrice):
    if len(prices) == 0:
        return 0
    maxDiff = 0
    for price in prices:
        if price-thePrice > maxDiff:
            maxDiff = price-thePrice
    laterDiff = maxProfitHelper(prices[1:],prices[0])
    return max(maxDiff, laterDiff)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def toArray(self):
        temp = []
        while self:
            temp.append(self.val)
            self = self.next
        return temp
    
class Solution:
    stairsSteps = [0,1,2]
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
    def addBinary(self, a, b):
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry //= 2

        return ''.join(reversed(s))
    def mySqrt(self, number):
        # brute force
        # i = 0
        # while i*i <= number:
        #     i+=1
        # return i-1
        # binary search method with half list optimization
        if (number == 0 or number == 1):
            return number
        l = 1
        r = number // 2 # squared result cannot be twice big
        while l <= r:
            mid = (l+r)//2
            powMid = mid*mid
            if powMid == number:
                return mid
            elif powMid > number:
                r = mid-1
            elif powMid < number:
                l = mid+1
                result = mid
        return result
    def climbStairs(self, n): # dynamic programming solution
        if len(self.stairsSteps) > n:
            return self.stairsSteps[n]
        i = len(self.stairsSteps)-1
        for i in range(i, n):
            self.stairsSteps.append(self.stairsSteps[i]+self.stairsSteps[i-1])
        return self.stairsSteps[n]
    def uniqueLinkedList(self, head):
        temp = head
        while temp and temp.next:
            if temp.next.val == temp.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
    def majorityElement(self, nums): # frequency counter approach
        theDict = Counter(nums) # a bit faster
        majority = len(nums)/2
        result = nums[0]
        # theDict = dict()
        # for i in nums:
        #     theDict[i]=theDict.get(i,0)+1
        for key,value in theDict.items():
            if value > majority:
                result = key
        return result
    def maxProfit(self, prices): 
        # recursive brute force solution - big space complexity     
        # if len(prices) == 1:
        #     return 0
        # return maxProfitHelper(prices[1:],prices[0])
        
        # compare each element with smallest so far
        minElement = prices[0]
        maxDiff = 0
        for i in range(1,len(prices)):
            maxDiff = max(prices[i]-minElement, maxDiff)
            minElement = min(prices[i],minElement)
        return maxDiff
    def isPalindrome(self, input):
        input = ''.join(re.findall('[a-zA-Z0-9]',input)).lower()
        left = 0
        right = len(input)-1
            
        # ic(re.match('[a-zA-Z0-9]',input[left]))
        # ic(re.match('[a-zA-Z0-9]',input[right]))
        # return len(input)
        while left < right:
            if input[left]!=input[right]:
                return False
            left+=1
            right-=1
        return True
    def isPalindrome(self, input: str) -> bool:
        # two pointers solution
        input = ''.join(re.findall('[a-zA-Z0-9]',input)).lower()
        left = 0
        right = len(input)-1
            
        while left < right:
            if input[left]!=input[right]:
                return False
            left+=1
            right-=1
        return True
        # py-featured solution
        # input = ''.join(re.findall('[a-zA-Z0-9]',input)).lower()
        # reversed = list(input)
        # reversed.reverse()
        # reversed = ''.join(reversed)
        # return input == reversed
