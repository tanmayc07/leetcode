# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l, c = [], 0
        while head:
            l.append(head.val)
            c += 1
            head = head.next
        
        s, e = 0, c-1
        mx = 0
        for i in range(c//2):
            mx = max(mx, l[i]+l[c-1-i])
        return mx