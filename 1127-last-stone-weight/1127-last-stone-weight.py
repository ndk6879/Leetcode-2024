import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) < 2:
            return stones[-1]
        
        tmp = []
        for num in stones:
            tmp.append(num * -1)

        heapq.heapify(tmp)

        while (len(tmp)>0):
            print('tmp:',tmp)
            if len(tmp) == 1:
                return tmp[-1] * -1
            x = heapq.heappop(tmp) * -1
            y = heapq.heappop(tmp) * -1
            print(tmp, x,y,'\n')
            if x != y:
                tmp.append(abs(x-y) * -1)

        return 0


