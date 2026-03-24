'''
- timestamp보다 작으면, 더큰 가능한 답이 있는지 확인하기 위해 오른쪽을 탐색 해야함. 
= 만약 timestamp보다 크다면 현재 값이 (timestamp보다 작아야 하기 때문에), r = mid - 1
'''
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