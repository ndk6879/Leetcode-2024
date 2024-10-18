from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        for num in sorted(counter, key = abs):
            if counter[num] > counter[num*2]:
                return False
            counter[num*2] -= counter[num]
        return True