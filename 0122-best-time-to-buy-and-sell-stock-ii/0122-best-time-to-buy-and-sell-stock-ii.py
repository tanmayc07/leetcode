class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for p in range(len(prices)):
            if p>0 and prices[p-1]<prices[p]:
                profit += prices[p]-prices[p-1] 

        return profit