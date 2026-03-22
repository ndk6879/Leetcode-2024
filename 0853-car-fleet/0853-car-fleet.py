class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        time = []

        for i in zip(position,speed):
            time.append(i)
        
        time.sort()
        stack = []

        while time:
            cur = time.pop()
            p,s = cur[0], cur[1]
            t = (target - p) / s

            if stack == [] or stack[-1] < t:
                ans += 1
            stack.append(t)
        return ans