# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        if not root.left and not root.right: return 1

        leftH = self.minDepth(root.left)
        rightH = self.minDepth(root.right)

        if not root.left or not root.right:
            return 1 + max(leftH, rightH)

        return 1 + min(leftH, rightH)