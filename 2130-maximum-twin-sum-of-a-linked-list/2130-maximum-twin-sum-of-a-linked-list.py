# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        dum = slow.next
        prev = None
        while dum:
            t = dum.next
            dum.next = prev
            prev = dum
            dum = t
        
        slow.next = prev
        
        st = head
        end = slow.next
        mx = 0
        while end:
            mx = max(mx, st.val+end.val)
            st = st.next
            end = end.next

        return mx