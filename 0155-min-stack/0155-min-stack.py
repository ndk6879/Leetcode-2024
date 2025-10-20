class MinStack:

    def __init__(self):
        self.arr = []
        self.Minarr = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)

        if self.Minarr == []:
            self.Minarr.append(val)
        
        else:
            minimum = min(val, self.Minarr[-1])
            self.Minarr.append(minimum)
            



    def pop(self) -> None:
        self.arr.pop()
        self.Minarr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.Minarr[-1] if len(self.Minarr) > 0 else []
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()