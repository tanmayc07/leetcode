# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0

    def height(self, root) -> int:
        if not root: return 0

        hL = self.height(root.left)
        hR = self.height(root.right)
        self.res = max(self.res, hL+hR)
        
        return 1 + max(hL, hR)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        
        return self.res