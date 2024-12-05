"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        if not node: return 
        d = {node : Node(node.val)}

        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for n in cur.neighbors:
                if n not in d:
                    d[n] = Node(n.val)
                    queue.append(n)
                d[cur].neighbors.append(d[n])
                
                
                
        return d[node]