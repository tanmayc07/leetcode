class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        t = sum(range(0, len(nums)+1))
        s = sum(nums)
        return t-s