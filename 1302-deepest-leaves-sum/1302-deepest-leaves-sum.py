# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = [root]
    
        s = 0
        while q:
            sz = len(q)
            s = 0
            while sz:
                r = q.pop(0)
                s += r.val
                if r.left: q.append(r.left)
                if r.right: q.append(r.right)
                sz -= 1

        return s
