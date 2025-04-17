class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, j, mp, rl = 0, 0, {}, 10**5
        res = ""

        for ind in t:
            mp[ind] = mp.get(ind, 0) + 1
        
        cnt = len(mp)
        while j<len(s):
            if s[j] in mp:
                mp[s[j]]-=1
                if mp[s[j]] == 0:
                    cnt -= 1
            
            while cnt==0:
                if j-i+1 < rl:
                    rl = min(rl, j-i+1)
                    res = s[i:j+1]

                if s[i] in mp:
                    mp[s[i]]+=1
                    if mp[s[i]]>0:
                        cnt+=1
                i+=1
            j+=1
        return res
