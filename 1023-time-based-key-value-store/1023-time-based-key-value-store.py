class TimeMap:

    def __init__(self):
        self.cache = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = [[value,timestamp]]
        
        else:
            self.cache[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.cache.get(key,[])

        l, r = 0, len(values)-1
        ans = ''
        while(l<=r):
            mid = (l+r) // 2
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return ans


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)