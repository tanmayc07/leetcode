class Solution:
    def mirrorFrequency(self, s: str) -> int:
        ch = [0]*26
        dg = [0]*10
        
        for c in s:
            if c.isalpha(): ch[ord('z')-ord(c)] += 1
            else: dg[ord('9')-ord(c)] += 1
        
        sm = 0
        for i in range(5): sm += abs(dg[i]-dg[9-i])
        for i in range(13): sm += abs(ch[i]-ch[26-i-1])

        return sm
        