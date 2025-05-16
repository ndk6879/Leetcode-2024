class MinStack:

    def __init__(self):
        self.stack = []
        self.Minarr = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.Minarr == []: self.Minarr.append(val)
        else:
            minVal = min(self.Minarr[-1],val)
            self.Minarr.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.Minarr.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Minarr[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()