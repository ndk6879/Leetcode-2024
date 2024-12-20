from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 필요한 문자 카운트
        s1Cnt = Counter(s1)
        # 현재 슬라이딩 윈도우의 문자 카운트
        windowCnt = Counter()
        
        n, m = len(s1), len(s2)
        
        for i in range(m):
            # 윈도우에 새로운 문자 추가
            windowCnt[s2[i]] += 1
            
            # 윈도우 크기가 s1과 같아지면 왼쪽 문자 제거
            if i >= n:
                windowCnt[s2[i - n]] -= 1
            
            # 현재 윈도우와 s1의 문자 카운트가 같으면 True 반환
            if windowCnt == s1Cnt:
                return True
        
        return False
