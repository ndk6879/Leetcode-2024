class MyStack:

    def __init__(self):
        self.queue1 = deque([])
        self.queue2 = deque([])
        

    def push(self, x: int) -> None:
        self.queue1.append(x)
        

    def pop(self) -> int:
        while(len(self.queue1) > 1):
            self.queue2.append(self.queue1.popleft())
            
        ans = self.queue1.popleft()
        print('POPPOP self.queue1:',self.queue2)
        self.queue1, self.queue2 = self.queue2, self.queue1
        print('POP self.queue1:',self.queue1)

        return ans
        

    def top(self) -> int:
        while(len(self.queue1) > 1):
            self.queue2.append(self.queue1.popleft())
        ans = self.queue1[0]
        self.queue2.append(self.queue1.popleft())
        # queue1과 queue2 교환
        self.queue1, self.queue2 = self.queue2, self.queue1
        return ans
        

    def empty(self) -> bool:
        print('EMPTY self.queue1:',self.queue1)
        return len(self.queue1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()