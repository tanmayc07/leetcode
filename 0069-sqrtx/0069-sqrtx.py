class Solution:
    def mySqrt(self, x: int) -> int:
        if x<1:
            return 0

        for i in range(1, x//2+2):
            if i*i > x:
                return i-1

            if i*i == x:
                return i