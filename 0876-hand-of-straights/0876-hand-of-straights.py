import heapq
from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False  # 그룹을 정확히 나눌 수 없으면 False
        
        count = Counter(hand)  # 숫자의 빈도수를 저장
        min_heap = list(count.keys())
        heapq.heapify(min_heap)  # 최소 힙 생성

        while min_heap:
            first = min_heap[0]  # 현재 가장 작은 값부터 그룹을 만듦
            
            for i in range(first, first + groupSize):  # groupSize만큼 연속된 수가 있어야 함
                if count[i] == 0:
                    return False  # 연속된 숫자가 없으면 실패
                
                count[i] -= 1  # 해당 숫자 사용
                
                if count[i] == 0:
                    if min_heap[0] != i:
                        return False  # 힙에서 제거할 숫자가 아니면 실패
                    heapq.heappop(min_heap)  # 힙에서 제거
        
        return True
