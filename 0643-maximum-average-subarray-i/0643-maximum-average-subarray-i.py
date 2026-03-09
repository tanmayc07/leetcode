class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_avg = window_sum/k

        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right-k]
            max_avg = max(max_avg, window_sum/k)

        return max_avg