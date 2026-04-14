from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        '''
        use heap to find max freq -> so we can use the most frequent one first to minize CPU
        '''

        counter = Counter(tasks)
        heap = [-task for task in counter.values()] #[-3, -3]
        print('heap:',heap)
        heapq.heapify(heap)
        arr = deque([])
        time = 0

        while heap or arr:
            time += 1

            if heap:
                cur = heapq.heappop(heap)
                print('cur:',cur)

                if cur + 1 != 0 :
                    arr.append([cur+1, time + n]) #[ [-2,3] ]

            if arr and arr[0][-1] == time:
                cur = arr.popleft()
                heapq.heappush(heap,cur[0])

        return time