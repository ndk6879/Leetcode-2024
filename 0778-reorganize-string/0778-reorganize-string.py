from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        print('count:',count)
        maxHeap = [[-freq,char] for char,freq in count.items() ]
        res = ''
        prev = [0,'']
        heapq.heapify(maxHeap)

        while maxHeap:
            if prev and not maxHeap:
                return ""
                
            freq, char =  heapq.heappop(maxHeap)
            res += char
            if prev[0] < 0:
                heapq.heappush(maxHeap,prev)
            prev = [freq + 1 , char]

        return res if len(res) == len(s) else ""  # \U0001f539 최종 길이 체크
