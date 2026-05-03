class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return False if (goal not in s+s) or len(s) != len(goal) else True
