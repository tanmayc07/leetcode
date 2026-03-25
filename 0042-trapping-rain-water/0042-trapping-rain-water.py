class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n

        curr_max = 0
        for i in range(n):
            max_left[i] = curr_max
            curr_max = max(curr_max, height[i])
        
        curr_max = 0
        for i in range(n-1,-1,-1):
            max_right[i] = curr_max
            curr_max = max(curr_max, height[i])

        total_trapped = 0
        for i in range(n):
            curr = min(max_left[i], max_right[i]) - height[i]
            if curr >= 0:
                total_trapped += curr

        return total_trapped