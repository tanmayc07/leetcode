# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [root]

        while q:
            sz = len(q)
            cl = {}
            while sz:
                c = q.pop(0)
                if c.left: 
                    q.append(c.left)
                    cl[c.left.val] = c.val
                if c.right: 
                    q.append(c.right)
                    cl[c.right.val] = c.val
                sz -= 1
            if (x in cl and y in cl) and (cl[x]!=cl[y]): return True
            

        return False

