class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        ans = []

        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]

        for i in range(len(nums)):
            ans.append(pre[i]*suf[i])

        return ans