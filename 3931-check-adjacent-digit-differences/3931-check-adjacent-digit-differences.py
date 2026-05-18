class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        l = [int(x) for x in s]
        for i in range(1, len(l)):
            if abs(l[i]-l[i-1]) > 2: return False
        return True