# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ans = None

        def dfs(root):
            if not root: return
            dfs(root.left)
            if root.val == target.val: self.ans = root
            dfs(root.right)

        dfs(cloned)
        return self.ans