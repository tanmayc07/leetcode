class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, 0
        sm = 0
        largest = float(-inf)
        while j < len(nums):
            sm += nums[j]
            if j - i + 1 < k:
                j+=1
            elif j - i + 1 == k:
                avg = sm / k
                largest = max(largest, avg)
                sm -= nums[i]
                j += 1
                i += 1
        
        return largest