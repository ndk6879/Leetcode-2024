from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        sCounter = Counter(s)
        maxHeap = [[-freq, char] for char, freq in sCounter.items()  ]
        heapq.heapify(maxHeap)
        ans = ''
        prev = [0, '']

        while maxHeap:
            if prev and not maxHeap:
                return ''
            freq, char = heapq.heappop(maxHeap)
            ans += char

            if prev[0] < 0:
                heapq.heappush(maxHeap, prev)
                
            prev = [freq+1,char]
                

        return ans if len(ans) == len(s) else ""