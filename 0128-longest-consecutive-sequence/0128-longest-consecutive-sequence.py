class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        largest = 0

        for num in hs:
            if num-1 not in hs:
                curr = num
                while curr in hs:
                    curr += 1
                largest = max(largest, curr-num)
        
        return largest
