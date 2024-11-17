from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque([])        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        cur = self.queue.pop()
        return cur

    def top(self) -> int:
        cur = self.queue[-1]
        return cur
        

    def empty(self) -> bool:
        print('self.queue:',self.queue, self.queue == [])
        return len(self.queue) == 0
        
[1,2,3,4]
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()