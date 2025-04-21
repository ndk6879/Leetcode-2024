import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        arr = []
        for x,y in points:
            distance = x ** 2 + y ** 2
            arr.append([distance,x,y])

        heapq.heapify(arr)

        ans = []
        while k > 0:
            cur = heapq.heappop(arr)
            ans.append([cur[1] ,cur[2] ])
            k -= 1
        return ans