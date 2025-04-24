class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0

        while right<len(nums):
            if right == len(nums)-1 or nums[right+1] != nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right+=1
            else:
                right+=1
        
        return left
            