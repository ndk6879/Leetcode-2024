import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[-1]
        new = []
        for s in stones:
            new.append(-s)
        
        heapq.heapify(new)
        print('newArr:',new)

        while (len(new) > 0):
            if len(new) == 1:
                return new[-1] * -1
                
            x = heapq.heappop(new) * -1
            y = heapq.heappop(new) * -1
            if x != y:
                new.append(abs(x - y) * -1)

            
        return 0