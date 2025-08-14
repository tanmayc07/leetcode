# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def traverse(node):
            if node:
                return 1 + traverse(node.left) + traverse(node.right)
            else:
                return 0
        cnt = traverse(root)
        return cnt
