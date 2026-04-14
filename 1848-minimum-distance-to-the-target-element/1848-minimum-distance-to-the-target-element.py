class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        d = float('inf')
        i = 0
        while i<len(nums):
            if nums[i] == target:
                d = min(d, abs(i-start))
            i += 1
        return d
