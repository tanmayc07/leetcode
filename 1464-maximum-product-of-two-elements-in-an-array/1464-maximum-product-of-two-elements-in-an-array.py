import heapq as hq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = [-x for x in nums]
        hq.heapify(heap)
        n1 = -hq.heappop(heap) - 1
        n2 = -hq.heappop(heap) - 1
        return n1 * n2