# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, st):
            if not node:
                return "~"
            
            st += chr(ord('a') + node.val)
            if not node.left and not node.right:
                return st[::-1]
            
            left = dfs(node.left, st) if node.left else "~"
            right = dfs(node.right, st) if node.right else "~"

            return min(left, right)
        
        return dfs(root, "")
        