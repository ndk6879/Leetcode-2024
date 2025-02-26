import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:

        sCounter = Counter(s)
        heap = [[ -1*freq, char  ] for char, freq in sCounter.items()]
        heapq.heapify(heap)
        prev = [0,'']
        ans = ''
        print('heap:',heap)

        while heap:
            freq, char = heapq.heappop(heap)
            print('freq:',freq, 'char:',char)
            ans += char

            if prev[0] < 0:
                heapq.heappush(heap,prev)

            prev = [1+freq, char]
            
        return ans if len(ans) == len(s) else ""