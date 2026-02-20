class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0

        for i in range(len(s)):
            stset = set()
            for j in range(i, len(s)):
                if s[j] in stset:
                    break
                stset.add(s[j])
                best = max(len(stset), best)

        return best