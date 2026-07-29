# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def H(self, root):
        if not root: return 0

        return 1 + max(self.H(root.left), self.H(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        leftH = self.H(root.left)
        rightH = self.H(root.right)

        return abs(leftH - rightH) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)