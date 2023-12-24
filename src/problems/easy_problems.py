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
        
sol = Solution()
print(sol.minOperations("01001"), 2)
print(sol.minOperations("0100"), 1)
print(sol.minOperations("1111"), 2)
print(sol.minOperations("000"), 1)
print(sol.minOperations("10"), 0)
print(sol.minOperations("0"), 0)
        
# print(sol.maxScore("011101"), 5)
# print(sol.maxScore("00111"), 5)
# print(sol.maxScore("1111"), 3)
# print(sol.maxScore("00"), 1)

# print(sol.maxScore("01"), 3)
# print(sol.maxScore("11"), 3)
# print(sol.maxScore("10"), 3)

# print(sol.twoSum([2,7,11,15], 9), [0,1])
# print(sol.twoSum([3,2,4], 6), [1,2])
# print(sol.twoSum([0,0,0,3,0,0,0,4], 7), [3,7])

# print(sol.buyChoco([1,2,2], 3), 0)
# print(sol.buyChoco([3,2,3], 3), 3)

# print(sol.maxProductionDifference([5,6,2,7,4]))
# print(sol.maxProductionDifference([4,2,5,9,7,4,8]))
# print(sol.maxProductionDifference([]))
# print(sol.maxProductionDifference([1,2]))
# print(sol.maxProductionDifference([1,2,3]))