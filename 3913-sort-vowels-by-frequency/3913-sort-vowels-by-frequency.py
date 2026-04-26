class Solution:
    def sortVowels(self, s: str) -> str:
        v = defaultdict(int)
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                v[s[i]] += 1
        v = sorted(v.items(), key=itemgetter(1), reverse=True)
        
        vc = []
        for e in v:
            for j in range(e[1]):
                vc.append(e[0])  

        vp = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                s[i] = vc[vp]
                vp += 1

        return "".join(s)