class MinStack:

    def __init__(self):
        self.stack = []
        self.Minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        val = min(val, self.Minstack[-1] if self.Minstack else val)
        self.Minstack.append(val)

        

    def pop(self) -> None:
        self.stack.pop()
        self.Minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.Minstack) > 0: 
            return self.Minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()