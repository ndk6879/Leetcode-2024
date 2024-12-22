class TimeMap:

    def __init__(self):
        self.hashMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = [[timestamp, value]]
        else:
            self.hashMap[key].append([timestamp, value])

    
    def get(self, key: str, timestamp: int) -> str:
        values = self.hashMap.get(key, [])
        l, r = 0, len(values) - 1
        ans = ''

        while(l<=r):
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                ans = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return ans

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)