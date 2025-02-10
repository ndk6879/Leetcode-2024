import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        newArr = []

        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            distance = (x**2 + y**2) ** .5
            newArr.append([distance,x,y])

        
        heapq.heapify(newArr)
        ans = []
        while (k > 0):
            cur = heapq.heappop(newArr)
            k -= 1
            ans.append([cur[1], cur[2]])
            if k == 0:
                return ans
