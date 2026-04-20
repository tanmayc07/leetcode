class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left, right = 0, 0

        for i in range(len(colors)):
            if colors[i] ^ colors[-1]:
                left = i
                break
        
        for i in range(len(colors)-1, -1, -1):
            if colors[i] ^ colors[0]:
                right = i
                break

        return max(len(colors)-left-1, right)