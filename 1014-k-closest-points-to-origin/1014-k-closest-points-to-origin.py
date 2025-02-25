import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        arr = []

        for x,y in points:
            dist = x**2 + y ** 2
            arr.append([dist, x, y])
            
        heapq.heapify(arr)
        ans = []
        while (k > 0):
            cur = heapq.heappop(arr)
            ans.append([cur[1], cur[2]])

            k -= 1
            if k == 0 :
                return ans