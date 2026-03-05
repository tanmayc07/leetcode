class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        found = 0
        if len(nums) == 1:
            return 0

        pre = [0] * len(nums)
        pos = [0] * len(nums)

        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] + nums[i]
        
        pos[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            pos[i] = pos[i+1] + nums[i]
        
        for i in range(len(nums)):
            if i == 0:
                left_sum = 0
                right_sum = pos[i+1]
            elif i == len(nums)-1:
                right_sum = 0
                left_sum = pre[i-1]
            else:
                left_sum = pre[i-1]
                right_sum = pos[i+1]
            
            if left_sum == right_sum:
                found = 1
                return i
            
        if found == 0:
            return -1
        
