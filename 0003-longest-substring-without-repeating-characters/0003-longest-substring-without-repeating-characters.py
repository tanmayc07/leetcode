class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        left = 0
        mx_len = 0
        
        for right in range(len(s)):
            while s[right] in mp:
                mp[s[left]] -= 1
                if not mp[s[left]]:
                    del mp[s[left]]
                left += 1

            mp[s[right]] += 1
            mx_len = max(mx_len, right-left+1)
        
        return mx_len
