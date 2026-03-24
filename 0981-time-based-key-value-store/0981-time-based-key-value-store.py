class TimeMap:

    def __init__(self):
        self.hash = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = [[value, timestamp]]
        else:
            self.hash[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ''
        if key not in self.hash:
            return ans

        l, r =0,len(self.hash[key]) - 1
        arr = self.hash[key]
        while (l <= r):
            mid = (l + r) // 2

            if arr[mid][1] <= timestamp:
                ans = arr[mid][0]
                l = mid + 1
            
            else:
                r = mid - 1
        
        return ans

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)