class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i, j, ml = 0, 0, -1
        mp = {}

        while j<len(nums):
            mp[nums[j]] = mp.get(nums[j], 0) + 1

            if mp[nums[j]] <= k:
                ml = max(ml, j-i+1)
            elif mp[nums[j]] > k:
                while mp[nums[j]] > k:
                    mp[nums[i]] -= 1
                    i += 1
            j += 1
        return ml