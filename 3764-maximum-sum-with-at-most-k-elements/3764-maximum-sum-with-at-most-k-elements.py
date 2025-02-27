import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        ans = []

        for i in range(len(grid)):
            cur = heapq.nlargest(limits[i], grid[i])
            ans += cur

        heapq.heapify(ans)
        print('ans:',ans)
        cur = heapq.nlargest(k, ans)
        return sum(cur)