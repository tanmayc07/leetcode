# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.s = 0
        def inord(root):
            if not root: return
            inord(root.right)
            self.s += root.val
            root.val = self.s
            inord(root.left)

        inord(root)
        return root