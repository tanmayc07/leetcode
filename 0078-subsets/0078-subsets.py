class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        all = []
        
        for mask in range(0, (1<<n)):
            subset = []
            for i in range(n):
                if (mask & (1<<i)) != 0:
                    subset.append(nums[i])
            all.append(subset)

        return all