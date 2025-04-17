class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i, j, ml, k = 0, 0, 0, 2
        mp = {}

        if len(fruits) == 1:
            return 1

        while j < len(fruits):
            mp[fruits[j]] = mp.get(fruits[j], 0) + 1

            if len(mp) <= k:
                ml = max(j-i+1, ml)
            elif len(mp) > k:
                while len(mp) > k:
                    mp[fruits[i]]-=1
                    if mp[fruits[i]] == 0:
                        del mp[fruits[i]]
                    i+=1
            j += 1
        return ml