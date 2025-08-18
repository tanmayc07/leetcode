class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}
        for i in range(len(s)):
            if s[i] in hm:
                hm[s[i]][0] += 1
                hm[s[i]][1] = i 
            else:
                hm[s[i]] = [1, i]
    
        mn = float('inf')
        for key, value in hm.items():
            if value[0] == 1 and value[1] < mn:
                mn = value[1]

        return mn if mn != float('inf') else -1

