# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []

        def dfs(node, sm, lst):
            if not node:
                return []
        
            lst.append(node.val)
            if not node.left and not node.right and sm == targetSum:
                res.append(list(lst))
            else:
                if node.left:
                    dfs(node.left, sm+node.left.val, lst)
                if node.right:
                    dfs(node.right, sm+node.right.val, lst)
            lst.pop()
        
        dfs(root, root.val, [])
        return res
        