class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        curr = Counter()
        left = 0

        for right in range(len(s2)):
            curr[s2[right]] += 1
            
            if right-left+1 == len(s1):
                if target == curr:
                    return True

                curr[s2[left]] -= 1
                if curr[s2[left]] == 0:
                    del curr[s2[left]]

                left += 1

        return False
            