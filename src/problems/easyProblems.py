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

sol = Solution()
print(sol.twoSum([2,7,11,15], 9), [0,1])
print(sol.twoSum([3,2,4], 6), [1,2])
print(sol.twoSum([0,0,0,3,0,0,0,4], 7), [3,7])

# print(sol.buyChoco([1,2,2], 3), 0)
# print(sol.buyChoco([3,2,3], 3), 3)

# print(sol.maxProductionDifference([5,6,2,7,4]))
# print(sol.maxProductionDifference([4,2,5,9,7,4,8]))
# print(sol.maxProductionDifference([]))
# print(sol.maxProductionDifference([1,2]))
# print(sol.maxProductionDifference([1,2,3]))