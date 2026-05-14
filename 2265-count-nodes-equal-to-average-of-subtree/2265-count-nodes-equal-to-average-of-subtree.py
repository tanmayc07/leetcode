# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(root):
            if not root: return 0, 0

            ls, lc = dfs(root.left)
            rs, rc = dfs(root.right)
            
            cs = root.val + ls + rs
            cc = 1 + lc + rc

            if cs//cc == root.val: self.ans += 1
            return cs, cc
        
        dfs(root)
        return self.ans

        