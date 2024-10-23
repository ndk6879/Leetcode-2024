
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