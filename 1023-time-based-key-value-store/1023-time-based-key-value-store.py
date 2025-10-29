from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hash = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append( [timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        l , r = 0, len(self.hash[key]) - 1
        value = ''

        while (l <= r):
            mid = (l + r) // 2

            if self.hash[key][mid][0] <= timestamp:
                value = self.hash[key][mid][1]
                l = mid + 1
            
            else:
                r = mid - 1
    
        return value
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)