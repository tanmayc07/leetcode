class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        res = []

        for i in range(len(strs)):
            st = "".join(sorted(strs[i]))
            if st not in hm:
                hm[st] = [strs[i]]
            else:
                hm[st].append(strs[i])
        
        for val in hm.values():
            res.append(val)
        
        return res