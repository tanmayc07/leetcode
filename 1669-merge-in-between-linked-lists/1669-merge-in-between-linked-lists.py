# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dum, t = ListNode(0, list1), list1
        prev = dum

        for i in range(a):
            prev = t
            t = t.next
        
        for i in range(b-a):
            t = t.next
        
        prev.next = list2
        while list2.next:
            list2 = list2.next
        
        list2.next = t.next
        return dum.next