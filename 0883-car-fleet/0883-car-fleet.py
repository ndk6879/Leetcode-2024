class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arr = []
        for p,s in zip(position,speed):
            arr.append((p,s))

        ans = []
        for i in sorted(arr)[::-1]:
            time = (target - i[0]) / i[1]

            ans.append(time)
            if len(ans) >= 2 and ans[-2] >= ans[-1]:
                ans.pop()

        return len(ans)