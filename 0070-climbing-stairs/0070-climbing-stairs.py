class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n


        arr = [0 for _ in range((n+1))]
        arr[0] = 1
        arr[1] = 1
        arr[2] = 2
        for i in range(2,n+1):
            arr[i] = arr[i-1] + arr[i-2]
        
        return arr[-1]