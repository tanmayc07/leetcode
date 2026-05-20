# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.val = root.val
        self.f = 1

        def dfs(root):
            if not root: return
            dfs(root.left)
            dfs(root.right)
            if root.val != self.val: self.f = 0
        
        dfs(root)
        return self.f == 1