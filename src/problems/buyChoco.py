class Solution:
    def buyChoco(self, prices, money):
        prices.sort()
        twoCheapestChocosPrices = prices[0] + prices[1]
        if (twoCheapestChocosPrices <= money):
            return money - twoCheapestChocosPrices
        return money
    
sol = Solution()
print(sol.buyChoco([1,2,2], 3), 0)
print(sol.buyChoco([3,2,3], 3), 3)