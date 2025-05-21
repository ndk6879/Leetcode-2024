from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.hashMap[key]) - 1
        ans = ''
        if key not in self.hashMap: return ''

        while (l <= r):
            mid = (l + r) // 2
            if self.hashMap[key][mid][0] <= timestamp:
                ans = self.hashMap[key][mid][1]
                l = mid + 1
            
            else:
                r = mid - 1
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)