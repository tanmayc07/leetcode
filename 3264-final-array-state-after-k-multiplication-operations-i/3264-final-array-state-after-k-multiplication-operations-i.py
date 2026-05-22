class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        q = []
        for i in range(len(nums)):
            heapq.heappush(q, [nums[i], i])
        
        while k:
            curr = heapq.heappop(q)
            heapq.heappush(q, [curr[0]*multiplier, curr[1]])
            k -= 1
        
        res = [0]*len(nums)
        while q:
            curr = heapq.heappop(q)
            res[curr[1]] = curr[0]
        
        return res
