class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        pmap = Counter(p)
        window_state = {}
        result = []

        for right in range(len(s)):
            window_state[s[right]] = window_state.get(s[right], 0) + 1
            
            if right - left + 1 == len(p):
                if pmap == window_state:
                    result.append(left)
                
                window_state[s[left]] = window_state.get(s[left]) - 1
                if window_state[s[left]] == 0:
                    del window_state[s[left]]
                left += 1
        
        return result
