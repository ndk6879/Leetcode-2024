class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)  # 문자 빈도수 계산
        maxHeap = [(-freq, char) for char, freq in count.items()]  # 최대 힙 만들기
        heapq.heapify(maxHeap)  # 힙 변환

        if any(-freq > (len(s) + 1) // 2 for freq, _ in maxHeap):  
            return ""  # 불가능한 경우 (가장 많은 문자 개수가 절반 초과)

        res = []
        prev = (0, "")  # 이전 문자를 저장할 변수 (빈도, 문자)

        while maxHeap:
            freq, char = heapq.heappop(maxHeap)  # 가장 빈도 높은 문자 꺼내기
            res.append(char)  # 결과 문자열에 추가

            if prev[0] < 0:  # 이전 문자가 남아있다면 다시 힙에 넣음
                heapq.heappush(maxHeap, prev)

            prev = (freq + 1, char)  # 사용한 문자 업데이트 (빈도 증가)

        return "".join(res)  # 리스트를 문자열로 변환하여 반환