class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m1 = {}
        for l in magazine:
            m1[l] = m1.get(l, 0) + 1
        
        for l in ransomNote:
            if m1.get(l, 0) == 0:
                return False
            m1[l] -= 1
        
        return True