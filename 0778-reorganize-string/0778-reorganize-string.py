import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        ans = ''
        counter = Counter(s)
        heap = []

        for string in counter:
            print(string,counter[string])
            heapq.heappush(heap,[counter[string] * -1 , string ])

        tmp = [0, '']
        while heap:
            cnt, string = heapq.heappop(heap)
            print(cnt,string)
            if tmp[0] < 0:
                heapq.heappush(heap,tmp)

            tmp = [cnt + 1, string]


            ans += string
        return ans if len(ans) == len(s) else ""