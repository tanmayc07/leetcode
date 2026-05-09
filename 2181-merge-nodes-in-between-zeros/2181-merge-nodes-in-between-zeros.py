# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum, t = ListNode(0, head), head.next
        start = dum

        l = []
        while t:
            l.append(t.val)
            if t.val == 0:
                s = sum(l)
                new = ListNode(s, t.next)
                start.next = new
                start = new
                t = t.next
                l = []
            else: t = t.next
        
        return dum.next
                 