class Solution:
    def climbStairs(self, n: int) -> int:
        # [0,1,2,3,5]
        if n <= 2:
            return n
        arr = [0] * (n+1)
        arr[1], arr[2] = 1, 2
        for i in range(3,len(arr)):
            arr[i] = arr[i-1] + arr[i-2]

        return arr[-1]