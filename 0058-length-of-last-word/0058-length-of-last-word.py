class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, ind = 0, 0
        s = s.strip()
        if len(s) == 1:
            return 1
        while i < len(s):
            ind = i+1 if s[i] == ' ' else ind
            i+=1
        return len(s[ind:])
