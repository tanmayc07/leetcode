# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        dummy = ListNode(0, head)
        p1 = head
        p2 = head.next
        newH = p2
        prev = dummy

        while p2 and p1.next:
            p1.next = p2.next
            p2.next = p1
            prev.next = p2
            prev = p1
            p1 = p1.next
            p2 = p1.next if p1 else None
        
        return newH