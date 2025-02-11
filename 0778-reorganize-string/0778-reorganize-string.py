from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)  # 문자 빈도수 계산
        maxHeap = [(-freq, char) for char, freq in count.items()]  # 최대 힙 만들기
        heapq.heapify(maxHeap)  # 힙 변환

        res = ""  # 결과 문자열을 저장할 변수
        prev = (0, "")  # 이전 문자를 저장할 변수 (빈도, 문자)

        while maxHeap:
            freq, char = heapq.heappop(maxHeap)  # 가장 빈도 높은 문자 꺼내기
            res += char  # 문자열에 추가

            if prev[0] < 0:  # 이전 문자가 남아있다면 다시 힙에 넣음
                heapq.heappush(maxHeap, prev)

            prev = (freq + 1, char)  # 사용한 문자 업데이트 (빈도 증가)

        # \U0001f6d1 힙이 비었는데 prev에 문자가 남아 있으면 불가능한 경우!
        return res if len(res) == len(s) else ""
