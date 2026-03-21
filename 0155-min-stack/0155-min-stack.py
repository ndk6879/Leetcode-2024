class MinStack:

    def __init__(self):
        self.arr = []
        self.Min = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)

        if self.Min == []:
            self.Min.append(val)
        
        else:
            self.Min.append(min(self.Min[-1],val))
        

    def pop(self) -> None:
        self.arr.pop()
        self.Min.pop()
        
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.Min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()