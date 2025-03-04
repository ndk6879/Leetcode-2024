import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        arr = []

        for i in range(len(grid)):
            arr += heapq.nlargest(limits[i] , grid[i])
            
        heapq.heapify(arr)


        return sum(heapq.nlargest(k,arr))
