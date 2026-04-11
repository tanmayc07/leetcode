import math

class Solution:
    def calc_hours(self, piles, k):
        h = 0
        for p in piles:
            h += math.ceil(p/k)
        return h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_k = max(piles)

        while left<=right:
            mid = left + (right-left)//2
            if self.calc_hours(piles, mid) <= h:
                min_k = min(min_k, mid)
                right = mid - 1
            else: left = mid+1
        
        return min_k
