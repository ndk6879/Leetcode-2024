from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # store indices

        for i in range(len(nums)):
            # 1. 윈도우 벗어난 인덱스 제거
            if q and q[0] <= i - k:
                q.popleft()

            # 2. 현재 값보다 작거나 같은 인덱스는 뒤에서 제거
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # 3. 첫 윈도우가 만들어진 시점부터 최대값 기록
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
