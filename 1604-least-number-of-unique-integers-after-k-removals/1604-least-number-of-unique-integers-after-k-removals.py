import heapq
from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        counter = Counter(arr)
        heap = list(counter.values())

        heapq.heapify(heap)

        ans = len(heap)
        while k and heap:
            f = heapq.heappop(heap)
            if k - f >= 0:
                k -= f
                ans -= 1
        
        return ans
