# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.s = 0
        def dfs(root):
            if not root: return
            dfs(root.left)
            if low<=root.val<=high: self.s+=root.val
            dfs(root.right)

        dfs(root)
        return self.s