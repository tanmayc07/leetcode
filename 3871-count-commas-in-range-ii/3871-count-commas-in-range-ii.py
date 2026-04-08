class Solution:
    def countCommas(self, n: int) -> int:
        cnt = 0
        divisor = 1000

        while n>=divisor:
            cnt += n-divisor+1
            divisor *= 1000
        
        return cnt

