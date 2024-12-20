from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Cnt = Counter(s1)
        windowCnt = Counter()
        l = 0  # 윈도우의 시작점
        
        for r in range(len(s2)):  # r은 윈도우의 끝점
            # 윈도우에 새 문자 추가
            windowCnt[s2[r]] += 1
            
            while r - l + 1 > len(s1):
                windowCnt[s2[l]] -= 1
                l += 1  # 윈도우의 시작점을 한 칸 오른쪽으로 이동
            
            # 윈도우와 s1의 문자 카운트 비교
            if windowCnt == s1Cnt:
                return True
        
        return False
