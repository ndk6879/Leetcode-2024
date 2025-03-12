class TimeMap:

    def __init__(self):
        self.hash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = [[timestamp, value]]
        else:
            self.hash[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hash:
            return ''
        
        l, r = 0, len(self.hash[key]) - 1
        ans = ''
        while(l <= r):
            mid = (l + r) // 2
            values = self.hash[key][mid]
            if values[0] <= timestamp:
                ans = values[1]
                l = mid + 1

            else:
                r = mid - 1
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)