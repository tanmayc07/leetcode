# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        h1, h2 = head, head
        p = None
        while h2 and h2.next:
            p = h1
            h1 = h1.next
            h2 = h2.next.next
        
        curr = h1
        p.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        h1 = prev

        first, second = head, h1
        tail = None
        while first and second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            tail = second
            first, second = t1, t2

        if second:
            tail.next = second 