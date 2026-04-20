class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0
        for i in range(len(colors)):
            for j in range(i, len(colors)):
                if colors[i] != colors[j]: 
                    max_dist = max(max_dist, j-i)
        return max_dist