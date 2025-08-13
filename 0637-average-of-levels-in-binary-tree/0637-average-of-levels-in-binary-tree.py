from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dq = deque()
        res: List[float] = []

        dq.append(root)
        while dq:
            rt = 0
            cnt = 0
            for _ in range(len(dq)):
                curr = dq.popleft()
                if curr:
                    rt+=curr.val
                    cnt+=1
                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right)
            res.append(rt/cnt)
        return res