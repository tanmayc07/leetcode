# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        l = 0
        dum = head
        while dum:
            if dum.val == val: l+=1
            dum = dum.next
        
        d = ListNode(0, head)
        for i in range(l):
            dum = d
            prev = dum
            while dum.val != val:
                prev = dum
                dum = dum.next

            prev.next = dum.next
            dum.next = None

        return d.next

