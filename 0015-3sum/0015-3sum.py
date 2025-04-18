class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        if len(nums) == 3 and nums[0]+nums[1]+nums[2]==0:
            return [[nums[0], nums[1], nums[2]]]
        elif len(nums) == 3 and nums[0]+nums[1]+nums[2]!=0:
            return []
        else:
            for k in range(len(nums)-2):
                i = k+1
                j = len(nums)-1
                while i<j:
                    if nums[i]+nums[j]+nums[k] < 0:
                        i+=1
                    elif nums[i]+nums[j]+nums[k] > 0:
                        j-=1
                    else:
                        res.add((nums[i], nums[j], nums[k]))
                        i+=1
                        j-=1
                            
                k+=1
        return [list(r) for r in res]