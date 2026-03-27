class Node: 
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = self.prev = None
'''
- use cache { key : Node}
'''

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # {key : Node()}
        self.cap = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next , self.right.prev = self.right, self.left
        
    def remove(self, node):
        prv, nxt = node.prev, node.next 
        prv.next, nxt.prev = nxt, prv
        
        
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        nxt.prev = node
        prev.next = node
        node.next, node.prev = nxt, prev
        print(node.val, node.next.val, node.prev.val)

    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)