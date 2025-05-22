import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks)

        maxHeap = [-i for i in counter.values() ]
        queue = deque([])

        time = 0
        heapq.heapify(maxHeap)

        while maxHeap or queue:
            time += 1

            if maxHeap:
                cur = heapq.heappop(maxHeap)
                print('cur:',cur)
                tmp = cur + 1

                if tmp != 0:
                    queue.append([tmp, time + n])

            if queue and queue[0][1] == time:
                cur = queue.popleft()
                heapq.heappush(maxHeap,cur[0])


        return time