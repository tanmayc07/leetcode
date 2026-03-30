class Solution:
    def trap(self, height: List[int]) -> int:
        p_max = [0]*len(height)
        s_max = [0]*len(height)
        curr = p_max[0] = height[0] 

        for i in range(1, len(height)):
            if height[i] > curr: 
                curr = height[i]
            p_max[i] = curr
        
        curr = s_max[-1] = height[-1] 
        for i in range(len(height)-1, -1, -1):
            if height[i] > curr:
                curr = height[i]
            s_max[i] = curr
        
        total_trapped = 0
        for i in range(len(height)):
            total_trapped += min(p_max[i], s_max[i]) - height[i]
        
        return total_trapped