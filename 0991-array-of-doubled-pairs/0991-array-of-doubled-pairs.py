class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import Counter
        counter = Counter(arr)
        
        for num in sorted(counter, key=abs):  # 절대값 기준으로 작은 수부터 확인
            if counter[num] > counter[2 * num]:
                return False
            counter[2 * num] -= counter[num]
        
        return True
