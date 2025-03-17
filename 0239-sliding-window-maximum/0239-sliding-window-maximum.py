from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # 숫자를 직접 저장
        l = r = 0

        while r < len(nums):
            # 1️⃣ 현재 숫자보다 작은 값들은 제거 (최댓값만 유지)
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])  # 현재 숫자 추가

            # 2️⃣ 윈도우에서 벗어난 값 제거 (왼쪽 값 제거)
            if r - l + 1 > k:  
                if nums[l] == q[0]:  # 윈도우에서 나갈 값이 최댓값이면 제거
                    q.popleft()
                l += 1  # 왼쪽 포인터 이동

            # 3️⃣ 정답 리스트에 추가 (윈도우 크기가 k일 때)
            if r >= k - 1:
                output.append(q[0])  # 덱의 맨 앞이 항상 최댓값
            r += 1  # 오른쪽 포인터 이동

        return output
