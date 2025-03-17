class TimeMap:

    def __init__(self):
        self.hash = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = [[timestamp, value]]
        else:
            self.hash[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        ans = 0
        if key not in self.hash: return ''

        l, r = 0, len(self.hash[key])-1
        ans = 0

        while (l <= r):
            mid = (l + r) // 2
            # print('self.hash[key][mid][0]:',self.hash[key])
            if self.hash[key][mid][0] <= timestamp:
                ans = self.hash[key][mid][1]
                l = mid + 1
            
            else:
                r = mid - 1
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)