class MinStack:

    def __init__(self):
        self.stack = []
        self.MinArray = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.MinArray:
            self.MinArray.append(val)

        else:
            minimum = min(self.MinArray[-1], val)
            self.MinArray.append(minimum)
        

    def pop(self) -> None:
        self.stack.pop()
        self.MinArray.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.MinArray[-1] 

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()