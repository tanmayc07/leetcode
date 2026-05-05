# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k: return head
        
        l = 1
        dum = head
        while dum.next != None:
            l += 1
            dum = dum.next
        
        r = k%l
        if r == 0: return head

        dum.next = head
        dum = head
        r = l-r-1
        while r:
            dum = dum.next
            r -= 1
        
        head = dum.next
        dum.next = None

        return head
