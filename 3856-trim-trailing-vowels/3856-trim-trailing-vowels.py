class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        inx = 0
        v = ['a','e','i','o','u']
        for i in range(len(s)-1, -1, -1):
            if s[i] not in v:
                inx = i
                break
            inx = i

        if inx == 0 and s[inx] in v:
            return ""
        return s[0:inx+1]
        