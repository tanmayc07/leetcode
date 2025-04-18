class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left = j+1
                right = len(nums)-1
                while left<right:
                    s = nums[left]+nums[right]+nums[i]+nums[j]
                    if s == target:
                        res.add((nums[left],nums[right],nums[i],nums[j]))
                        while left<right and nums[left+1]==nums[left]:
                            left+=1
                        while left<right and nums[right-1]==nums[right]:
                            right-=1
                        left+=1
                        right-=1
                    elif s < target:
                        left+=1
                    else:
                        right-=1
        return [list(r) for r in res]