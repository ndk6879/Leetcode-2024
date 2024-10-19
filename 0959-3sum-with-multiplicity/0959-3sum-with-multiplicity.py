from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = Counter(arr)
        keys = sorted(counter.keys())
        result = 0
        MOD = 10**9 + 7

        for i in range(len(keys)):
            x = keys[i]
            for j in range(i, len(keys)):
                y = keys[j]
                z = target - x - y
                if z < y:
                    continue
                if z in counter:
                    if x == y == z:  # 세 숫자가 모두 같은 경우
                        result += counter[x] * (counter[x] - 1) * (counter[x] - 2) // 6
                    elif x == y != z:  # 두 숫자가 같고 나머지가 다른 경우
                        result += counter[x] * (counter[x] - 1) // 2 * counter[z]
                    elif x != y and y == z:  # 첫 번째 숫자만 다르고 나머지 두 숫자가 같은 경우
                        result += counter[x] * counter[y] * (counter[y] - 1) // 2
                    elif x < y < z:  # 세 숫자가 모두 다른 경우
                        result += counter[x] * counter[y] * counter[z]

        return result % MOD