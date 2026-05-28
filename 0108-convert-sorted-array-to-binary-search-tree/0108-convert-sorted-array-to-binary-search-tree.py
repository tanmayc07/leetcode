# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start, end = 0, len(nums)-1

        def tree(nums, start, end):
            if start>end: return None

            mid = (start+end)//2

            root = TreeNode(nums[mid])

            root.left = tree(nums, start, mid-1)
            root.right = tree(nums, mid+1, end)
            
            return root

        root = tree(nums, start, end)
        return root