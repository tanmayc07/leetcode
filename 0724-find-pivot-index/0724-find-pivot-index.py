class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps = [0] * len(nums)
        suf = [0] * len(nums)

        for i in range(1, len(nums)):
            ps[i] = ps[i-1] + nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] + nums[i+1]

        for i in range(len(nums)):
            if ps[i] == suf[i]:
                return i
        
        return -1