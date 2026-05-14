class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)
        l = [i for i in range(1, mx+1)]
        l.append(mx)

        return sorted(nums) == l