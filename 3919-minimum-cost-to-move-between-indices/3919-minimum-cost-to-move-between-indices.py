class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        pre = [0]*n
        pos = [0]*n
        for i in range(n-1):
            if i==0 or abs(nums[i-1]-nums[i])>abs(nums[i+1]-nums[i]):
                pre[i+1] = pre[i]+1
            else:
                pre[i+1] = pre[i]+nums[i+1]-nums[i]
        
        for i in range(1,n):
            if i==n-1 or nums[i]-nums[i-1] <= nums[i+1]-nums[i]:
                pos[i] = pos[i-1]+1
            else:
                pos[i] = pos[i-1]+nums[i]-nums[i-1]

        res = []
        for l,r in queries:
            if l<r:
                res.append(pre[r]-pre[l])
            else:
                res.append(pos[l]-pos[r])
        return res
            