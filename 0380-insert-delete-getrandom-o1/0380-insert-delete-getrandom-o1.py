import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hash = {}
        self.index = 0

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False

        self.hash[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False

        # [3, 4, 5] -> [5, 4, 3] -> [5, 4]
        valIndex = self.hash[val]
        lastVal = self.arr[-1]

        # Move lastVal to the place of val
        self.arr[valIndex] = lastVal
        self.hash[lastVal] = valIndex  # \U0001f525 중요! 해시맵도 업데이트!

        # Remove last element
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