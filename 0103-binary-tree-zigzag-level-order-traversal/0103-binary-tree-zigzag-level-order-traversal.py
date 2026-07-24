# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        c = 1

        while q:
            ls = len(q)
            l = []

            for _ in range(ls):
                node = q.popleft()
                l.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            if not c%2: res.append(l[::-1])
            else: res.append(l)

            c += 1
        
        return res