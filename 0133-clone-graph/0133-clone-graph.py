"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return 
        d = {node : Node(node.val)}

        queue = deque([node])
        
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for i in cur.neighbors:
                    if i not in d:
                        d[i] = Node(i.val)
                        queue.append(i)

                    d[cur].neighbors.append(d[i])

        return d[node]