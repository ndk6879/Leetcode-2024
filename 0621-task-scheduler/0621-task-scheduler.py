from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks)

        maxHeap = [-cnt for cnt in counter.values()]
        queue = deque([]) # [cnt, idletime]
        heapq.heapify(maxHeap)

        time = 0
        while maxHeap or queue:
            time += 1

            if maxHeap:
                cur = heapq.heappop(maxHeap) + 1
                if cur != 0:
                    queue.append([cur, time+n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap,queue.popleft()[0])

        

        
        return time