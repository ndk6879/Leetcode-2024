class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        
    #[1,2,3,4,5] -> [1,2,3,4]
    def pop(self) -> int:
        if self.stack2 == []:
            while(self.stack1): #[1,2,3,4,5]
                self.stack2.append(self.stack1.pop()) #[5,4,3,2,1]
        
        return self.stack2.pop()
        

    def peek(self) -> int:
        if self.stack2 == []:

            while(self.stack1): #[1,2,3,4,5]
                self.stack2.append(self.stack1.pop()) #[5,4,3,2,1]
        
        return self.stack2[-1]
        

    def empty(self) -> bool:
        return max(self.stack2, self.stack1) == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()