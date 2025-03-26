from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        arr = [[-v,k] for k,v in counter.items()]
        heapq.heapify(arr)

        print('arr:',arr)

        ans = ''
        tmp = [0,'']
        while arr:
            cnt, character = heapq.heappop(arr)
            if tmp[0] < 0:
                heapq.heappush(arr,tmp)
            
            tmp = [cnt + 1,character]
            ans += character
            
            print('ans:',ans,'\narr:',arr,'\n')

        
        return ans if len(ans) == len(s) else ""