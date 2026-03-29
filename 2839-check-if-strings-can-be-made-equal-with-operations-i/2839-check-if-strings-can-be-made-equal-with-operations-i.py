class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s = list(s1)
        for i in range(2):
            if s[i] != s2[i]:
                s[i], s[i+2] = s[i+2], s[i]
            
        s1 = ''.join(s)

        if s1==s2: return True
        else: return False