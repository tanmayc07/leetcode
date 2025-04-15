class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, ml = 0, 0, -1
        mp = {}

        while j<len(s):
            mp[s[j]] = mp.get(s[j], 0) + 1

            if len(mp) == j-i+1:
                ml = max(ml, j-i+1)
            elif len(mp) < j-i+1:
                while len(mp) < j-i+1:
                    mp[s[i]] -= 1
                    if mp[s[i]] == 0:
                        del mp[s[i]]
                    i += 1
            j += 1
        return ml if ml>0 else 0
                