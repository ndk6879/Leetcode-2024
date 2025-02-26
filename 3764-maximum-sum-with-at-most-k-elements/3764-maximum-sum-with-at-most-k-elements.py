import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        arr = []

        for i in range(len(grid)):
            cur = heapq.nlargest(limits[i],grid[i])
            arr += cur

        heapq.heapify(arr)
        return sum(heapq.nlargest(k,arr))