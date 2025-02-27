from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = [ [-freq, char]  for char, freq in counter.items()]

        heapq.heapify(heap)
        print('heap:',heap)
        ans = ''
        prev = [0,'']
        while heap:
            freq,char = heapq.heappop(heap)
            ans += char
            print('ans:',ans, heap)
            if prev[0] < 0:
                heapq.heappush(heap,prev)


            prev = [freq+1 , char]
            
        return ans if len(ans) == len(s) else ""


        