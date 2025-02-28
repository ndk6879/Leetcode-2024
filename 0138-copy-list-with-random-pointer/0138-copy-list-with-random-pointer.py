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
        copyHash = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            copyHash[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            curCopy = copyHash[cur]
            curCopy.next = copyHash[cur.next]
            curCopy.random = copyHash[cur.random]
            cur = cur.next

        return copyHash[head]