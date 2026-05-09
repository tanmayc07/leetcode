# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        l = 0
        t = head
        while t:
            l += 1
            t = t.next

        s, t = 0, head
        for i in range(l-1, -1, -1):
            s += pow(2, i) if t.val else 0
            t = t.next
        
        return s