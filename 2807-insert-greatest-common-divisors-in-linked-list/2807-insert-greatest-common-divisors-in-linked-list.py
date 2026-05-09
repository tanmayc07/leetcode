# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return head
    
        p1, p2 = head, head.next
        while p2:
            gcd = 1
            for i in range(2, min(p1.val, p2.val)+1):
                if not p1.val%i and not p2.val%i: gcd = max(gcd, i)
            new = ListNode(gcd, p2)
            p1.next = new
            p1 = p2
            p2 = p2.next
        
        return head


