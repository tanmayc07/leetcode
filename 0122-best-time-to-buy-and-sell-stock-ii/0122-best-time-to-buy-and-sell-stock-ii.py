class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot = 0

        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                tot += prices[i+1]-prices[i]

        return tot