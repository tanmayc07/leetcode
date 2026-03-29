class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        idx = float('inf')
        for i in range(len(s)//2+1):
            if s[i] == s[len(s)-i-1]:
                idx = min(idx, i)

        return idx if idx != float('inf') else -1