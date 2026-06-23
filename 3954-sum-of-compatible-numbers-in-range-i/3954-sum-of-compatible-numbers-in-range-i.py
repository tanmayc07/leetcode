class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        com = []
        for i in range(n-k, n+k+1, 1):
            if i>0 and n & i == 0: com.append(i)

        return sum(com)