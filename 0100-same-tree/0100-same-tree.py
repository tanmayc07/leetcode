from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverse(node):
            tree = []
            dq = deque()
            dq.append(node)

            while dq:
                curr = dq.popleft()
                if curr:
                    tree.append(curr.val)
                    dq.append(curr.left) if curr.left else tree.append(100001)
                    dq.append(curr.right) if curr.right else tree.append(100002)
                    
            return tree

        tree1 = traverse(p)
        tree2 = traverse(q)

        return tree1 == tree2

                


                
