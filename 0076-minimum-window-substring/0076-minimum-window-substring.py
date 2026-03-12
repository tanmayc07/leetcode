class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        left = 0
        target_map = Counter(t)
        window_map = Counter()
        formed = 0
        min_len = (float("inf"), 0, 0)
        result = ""

        for right in range(len(s)):
            window_map[s[right]] += 1

            if window_map[s[right]] == target_map[s[right]]:
                formed += 1
            
            while formed == len(target_map):
                if right-left+1 < min_len[0]:
                    min_len = (right-left+1, left, right)

                window_map[s[left]] -= 1
                
                if window_map[s[left]] < target_map[s[left]]:
                    formed -= 1

                if window_map[s[left]] == 0:
                    del window_map[s[left]]
                
                
                left += 1
            
    
        return s[min_len[1]: min_len[2]+1] if min_len[0] != float("inf") else ""