class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        max_count = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_count = max(freq.values())

            while right - left + 1 - max_count > k:
                freq[s[left]] -= 1
                left += 1
                max_count = max(freq.values())
            
            max_len = max(max_len, right-left+1)
        
        return max_len
