class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        freq = Counter()
        s1freq = Counter(s1)

        for right in range(len(s2)):
            freq[s2[right]] += 1

            if right-left+1 == len(s1) :
                if freq == s1freq:
                    return True
            
                freq[s2[left]] -= 1
                if freq[s2[left]] == 0:
                    del freq[s2[left]]
                left += 1
        
        return False
                