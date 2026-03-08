class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        best = 0
        sset = set()

        for j in range(len(s)):
            while s[j] in sset:
                sset.remove(s[i])
                i += 1

            sset.add(s[j])
            best = max(best, j-i+1)

        return best