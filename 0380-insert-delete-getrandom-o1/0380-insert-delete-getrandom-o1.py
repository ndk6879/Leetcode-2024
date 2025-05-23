import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hash = {}

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False

        self.hash[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False

        # [1, 3, 4, 5] -> [1, 5, 4, 3] -> [1, 5, 4]
        
        targetIndex = self.hash[val]
        self.hash[self.arr[-1]] = targetIndex

        self.arr[targetIndex], self.arr[-1] = self.arr[-1], self.arr[targetIndex]

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