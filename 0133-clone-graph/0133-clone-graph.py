'''
2/9
bfs를 써서 푸는데 dictionary를 써서 neighbor를 저장.
d[current].neighbors.append(d[neighbor])를 해줘서 이웃이 뭔지 알게해줌.
time: O(V + E)
memory: O(V) for hashmap
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        
        d = {node:Node(node.val)}
        queue = deque([node])
        
        while queue:
            for i in range(len(queue)):
                current = queue.popleft()
                for neighbor in current.neighbors:
                    if neighbor not in d:
                        d[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)
                    d[current].neighbors.append(d[neighbor])
        return d[node]