from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        height = 0
        
        if not root:
            return height

        dq.append(root)

        while dq:
            for _ in range(len(dq)):
                curr = dq.popleft()
                if curr:
                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right)
            height += 1
        
        return height