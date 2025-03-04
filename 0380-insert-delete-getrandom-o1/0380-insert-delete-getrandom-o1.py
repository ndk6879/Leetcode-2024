class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val not in self.hashMap: 
            self.hashMap[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.hashMap: return False
        ind = self.hashMap[val]
        last = self.arr[-1]

        self.arr[ind] = last
        self.hashMap[last] = ind
        
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