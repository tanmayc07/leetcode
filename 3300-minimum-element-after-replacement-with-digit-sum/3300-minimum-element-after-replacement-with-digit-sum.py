class Solution:
    def minElement(self, nums: List[int]) -> int:
        mn = float('inf')
        
        for num in nums:
            n = num
            s = 0
            while n:
                s += n%10
                n = n//10
            mn = min(s, mn)

        return mn