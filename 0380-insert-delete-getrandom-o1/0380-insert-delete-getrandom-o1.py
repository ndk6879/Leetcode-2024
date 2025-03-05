class RandomizedSet:

    def __init__(self):
        self.hash = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.hash: return False
        self.hash[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hash: return False

        ind = self.hash[val]
        lastElement = self.arr[-1]
        self.arr[ind] = lastElement
        self.hash[lastElement] = ind
        self.arr.pop()
        del self.hash[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()