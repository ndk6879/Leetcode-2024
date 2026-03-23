class TimeMap:

    def __init__(self):
        self.hash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = [[value, timestamp]]
        else:
            self.hash[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash:
            return ""

        arr = self.hash[key]
        l, r = 0, len(arr) - 1
        ans = ""

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][1] <= timestamp:
                ans = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return ans