# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, res, st):
            if not node:
                return 
            st += str(node.val) + "->"
            if not node.left and not node.right:
                res.append(st[:-2])
            else:
                dfs(node.left, res, st)
                dfs(node.right, res, st)
        
        dfs(root, res, "")
        return res