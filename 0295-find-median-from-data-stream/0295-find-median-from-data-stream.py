import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []  # 최대 힙 (음수값 저장) → 왼쪽 절반
        self.minHeap = []  # 최소 힙 → 오른쪽 절반

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)  # -음수값 저장 → Python은 min-heap만 지원
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))  # 큰 값은 minHeap으로 이동

        if len(self.maxHeap) < len(self.minHeap):  # 균형 유지 (maxHeap이 항상 크거나 같아야 함)
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):  # 홀수 개일 때 → maxHeap 루트값이 중앙값
            return -self.maxHeap[0]
        else:  # 짝수 개일 때 → maxHeap과 minHeap 루트값 평균
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
