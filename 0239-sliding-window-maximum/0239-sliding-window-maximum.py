from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l, r =0, 0

        queue = deque([])
        ans = []
        while (r < len(nums)):

            #1. when prev is smaller 
            while (queue and nums[queue[-1]] < nums[r]):
                queue.pop()

            queue.append(r)

            #2. remove out of window
            if queue and l > queue[0]:
                queue.popleft()

            #3. d
            if (r + 1) >= k:
                ans.append(nums[queue[0]])
                l += 1

            r += 1

        return ans            