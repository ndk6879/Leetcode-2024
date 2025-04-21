import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[-1]

        newStones = []
        for stone in stones:
            newStones.append(-1*stone)
        heapq.heapify(newStones)

        while len(newStones) > 1:
            print('newStones:',newStones)
            x = -1*heapq.heappop(newStones)
            y = -1*heapq.heappop(newStones)

            if x == y:
                continue
            
            else:
                diff = abs(x-y) * -1
                heapq.heappush(newStones, diff)
        if newStones:
            if newStones[-1] > 0:
                return newStones[-1]
            else:
                return newStones[-1] * -1
        else:
            return 0