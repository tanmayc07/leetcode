class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq = 1
        find_uniq = 1

        while find_uniq < len(nums):
            if nums[find_uniq] != nums[uniq-1]:
                nums[uniq] = nums[find_uniq]
                uniq += 1
            
            find_uniq += 1
        
        return uniq
