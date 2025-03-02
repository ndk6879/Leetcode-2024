import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max-heap (Python은 min-heap만 지원하므로 음수값 저장)
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)  # max-heap처럼 사용하기 위해 음수로 저장
        heapq.heappush(self.large, -heapq.heappop(self.small))  # 큰 값은 large로 이동

        if len(self.small) < len(self.large):  # 균형 유지
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):  # 홀수 개일 때
            return -self.small[0]
        else:  # 짝수 개일 때
            return (-self.small[0] + self.large[0]) / 2
