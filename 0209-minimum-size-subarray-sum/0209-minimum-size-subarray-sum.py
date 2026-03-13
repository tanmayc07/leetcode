class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        win_sum = 0
        min_len = float("inf")

        for right in range(len(nums)):
            win_sum += nums[right]

            while win_sum >= target:
                win_sum -= nums[left]
                min_len = min(min_len, right-left+1)
                left += 1

        return min_len if min_len != float("inf") else 0