# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        def calc(root):
            if not root: return 0

            l = calc(root.left)    
            r = calc(root.right)

            self.res += abs(l-r)
            return l + r + root.val

        calc(root)
        return self.res