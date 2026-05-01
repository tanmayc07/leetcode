"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None:None}
        start = head
        while start:
            mp[start] = Node(start.val, None, None)
            start = start.next
        
        start = head
        while start:
            copy = mp.get(start)
            copy.next = mp.get(start.next)
            copy.random = mp.get(start.random)
            start = start.next
        
        return mp.get(head)