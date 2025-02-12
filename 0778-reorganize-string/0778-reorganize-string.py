from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxHeap = [[-freq, char] for char,freq in counter.items()]
        res = ''
        heapq.heapify(maxHeap)
        prev = [0,'']
        

        while maxHeap:
            if prev and not maxHeap:
                return ''
            freq, char = heapq.heappop(maxHeap)
            res += char

            if prev[0] < 0:
                heapq.heappush(maxHeap,prev)

            prev = [freq+1, char]

        return res if len(res) == len(s) else ""