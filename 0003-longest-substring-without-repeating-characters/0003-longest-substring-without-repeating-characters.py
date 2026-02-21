class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        for i in range(len(s)):
            sset = set()
            for j in range(i, len(s)):
                if s[j] in sset:
                    break
                sset.add(s[j])
            best = max(len(sset), best)
        return best