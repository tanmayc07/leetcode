class Solution:
    def minOperations(self, nums: list[int]) -> int:
        sx = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>nums[i+1]:
                sx += nums[i]-nums[i+1]
        return sx