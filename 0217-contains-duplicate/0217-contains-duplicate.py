class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}

        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
            if hm[nums[i]] > 1:
                return True
        
        return False
        
