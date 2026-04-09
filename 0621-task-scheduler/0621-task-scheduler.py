from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks)
        maxHeap = [-task for task in counter.values()] # [-3,-3]
        heapq.heapify(maxHeap)
        queue = deque([])

        time = 0
        while maxHeap or queue:
            time += 1
            
            if maxHeap:
                cur = heapq.heappop(maxHeap)

                if cur + 1 != 0:
                    queue.append([cur+1, time + n])

            if queue and queue[0][1] == time:
                cur = queue.popleft()
                heapq.heappush(maxHeap,cur[0])
        
        return time