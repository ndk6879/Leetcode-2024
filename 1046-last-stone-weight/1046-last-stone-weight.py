import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 1: return stones[0]
        
        arr = []
        for stone in stones:
            arr.append(-stone)
        
        heapq.heapify(arr)

        while len(arr) > 1:

            x, y = heapq.heappop(arr), heapq.heappop(arr)

        

            if x == y:
                continue

            else:
                heapq.heappush(arr,(x-y))
        
        return -arr[0] if arr else 0