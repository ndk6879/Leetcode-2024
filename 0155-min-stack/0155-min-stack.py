class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min:
            if self.min[-1] > val:
                self.min.append(val)
        
        else:
            self.min.append(val)
            

        

    def pop(self) -> None:
        self.stack.pop()
        if self.min:
            self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min:
            return self.min[-1]
        return self.stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()