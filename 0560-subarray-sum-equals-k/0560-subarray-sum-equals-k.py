class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        
        for i in range(len(nums)):
            sm = 0
            for j in range(i, len(nums)):
                sm += nums[j]
                if sm == k:
                    cnt += 1
        
        return cnt