# Definition for singly-linked list.
# class ListNode
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dum = head
        while dum != None and dum.next != None:
            while dum.next and dum.next.val == dum.val:
                temp = dum.next
                dum.next = dum.next.next
                temp.next = None
            dum = dum.next
        return head
