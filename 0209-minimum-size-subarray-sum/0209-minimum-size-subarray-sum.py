class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j, s, res = 0, 0, 0, 10**5
        f = 0

        while j < len(nums):
            s += nums[j]

            while s >= target:
                f = 1
                res = min(res, j-i+1)
                s -= nums[i]
                i += 1

            j += 1

        return 0 if f==0 else res
            