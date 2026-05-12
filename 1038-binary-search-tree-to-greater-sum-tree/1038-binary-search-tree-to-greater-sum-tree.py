# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ino = []
        def inord(root):
            if not root: return
            inord(root.left)
            ino.append(root.val)
            inord(root.right)

        inord(root)
        ts, cur = sum(ino), 0
        mp = {}
        for i in range(len(ino)):
            mp[ino[i]] = ts - cur
            cur += ino[i]
        
        def ino(root):
            if not root: return
            ino(root.left)
            root.val = mp[root.val]
            ino(root.right)
        
        ino(root)
        return root