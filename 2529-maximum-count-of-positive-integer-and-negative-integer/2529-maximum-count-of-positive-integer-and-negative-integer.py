class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] < 0: start = mid + 1
            else: end = mid - 1
        
        nc = start
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] < 1: start = mid + 1
            else: end = mid - 1
        
        pc = len(nums)-start

        return max(nc, pc) 