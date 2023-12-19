class Solution:
    def maxProductionDifference(self, nums):
        nums.sort()
        nums_size = len(nums)
        if (nums_size < 4):
            return 0
        return nums[nums_size-1]*nums[nums_size-2]-nums[0]*nums[1]
    
sol = Solution()
print(sol.maxProductionDifference([5,6,2,7,4]))
print(sol.maxProductionDifference([4,2,5,9,7,4,8]))
print(sol.maxProductionDifference([]))
print(sol.maxProductionDifference([1,2]))
print(sol.maxProductionDifference([1,2,3]))