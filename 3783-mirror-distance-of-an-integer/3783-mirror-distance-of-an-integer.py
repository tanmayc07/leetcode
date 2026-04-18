class Solution:
    def mirrorDistance(self, n: int) -> int:
        n1 = n
        rev = 0
        while n1:
            d = n1%10
            rev = rev*10 + d
            n1 = n1//10
        
        return abs(n-rev)