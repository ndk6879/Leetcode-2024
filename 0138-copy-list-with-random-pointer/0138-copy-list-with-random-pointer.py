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
        
        d = {None : None}
        
        dummy = head
        while dummy:
            d[dummy] = ListNode(dummy.val)
            dummy = dummy.next
        
        dummy = head
        while dummy:
            d[dummy].next = d[dummy.next]
            d[dummy].random = d[dummy.random]
            dummy = dummy.next

        return d[head]
