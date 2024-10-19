class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter

        if k < 0:
            return 0  # k가 음수이면 차이를 만족하는 쌍이 존재할 수 없음

        counter = Counter(nums)
        count = 0

        if k == 0:
            # k가 0일 때: 같은 숫자가 2개 이상 있는 경우만 세기
            for num in counter:
                if counter[num] > 1:
                    count += 1
        else:
            # k가 양수일 때: num + k가 존재하는지 확인
            for num in counter:
                if num + k in counter:
                    count += 1

        return count
