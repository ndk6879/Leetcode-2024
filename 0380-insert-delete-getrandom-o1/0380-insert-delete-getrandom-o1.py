class RandomizedSet:

    def __init__(self):
        self.hashMap = {} # to store val
        self.arr = [] # to sotre val and ind
        

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        
        self.hashMap[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hashMap: return False

        
        ind = self.hashMap[val]
        lastElement = self.arr[-1]

        self.arr[ind] = lastElement
        self.hashMap[lastElement] = ind

        self.arr.pop()
        del self.hashMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()