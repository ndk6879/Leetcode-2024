from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque([])
        l, r = 0,0
        ans = []

        while (r < len(nums)):

            #pop smaller value
            while (q and nums[q[-1]] < nums[r]):
                q.pop()

            q.append(r)

            #remove l out of window
            if (q and q[0] < l):
                q.popleft()

            #add in window
            if (r+1) >= k:
                ans.append(nums[q[0]])
                l += 1
            r += 1

        return ans