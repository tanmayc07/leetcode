class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mp = Counter(x % value for x in nums)
        
        x = 0
        while mp[x%value] > 0:
            mp[x%value] -= 1
            x += 1
        
        return x