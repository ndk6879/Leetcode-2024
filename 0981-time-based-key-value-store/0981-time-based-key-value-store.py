'''
- 어떤 키에 value를 추가함. 근데 매번 timestamnmp가 다름.
- get에서 어떤 timestamp값을 줌. 그 timestamp보다 작은애들중 젤큰애를 return해주면됨.
'''
class TimeMap:

    def __init__(self):
        self.hash = {} # {key : [timestamp,value]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = [[timestamp, value]]
        else:
            self.hash[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash:
            return ''
        l = 0 
        r = len(self.hash[key]) - 1
        value = ''
        while (l <= r):
            mid = (l + r) // 2
            curTime = self.hash[key][mid][0]
            print('curTime:',curTime)
            if curTime <= timestamp:
                value = self.hash[key][mid][1]
                l = mid + 1
            
            else:
                r = mid - 1
        return value

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)