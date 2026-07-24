# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res = []
        q = deque([root])

        while q:
            ls = len(q)
            l = []

            for _ in range(ls):
                node = q.popleft()
                l.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            res.append(l)
        
        return res[::-1]