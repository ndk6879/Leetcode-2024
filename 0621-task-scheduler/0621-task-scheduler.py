from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        '''
        - Count #
        - maxHeap = [] # [-3,-3]
        - queue = []
        while maxHepap and queue:
            time += 1
            if maxHeap:
                cur = maxHeap.heappop()

            queue.append([cur+1,time+n])
            if queue and queue[0][1] == time:
                queue.pop()
                task.heappush
        return ans

        '''

        counter = Counter(tasks)
        maxHeap = [-task for task in counter.values()]
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