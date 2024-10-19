from collections import Counter

class Solution:
    def threeSumMulti(self, arr, target):
        counter = Counter(arr)
        keys = sorted(counter.keys())
        result = 0
        MOD = 10**9 + 7

        for i in range(len(keys)):
            x = keys[i]
            for j in range(i, len(keys)):
                y = keys[j]
                z = target - x - y  # 세 번째 숫자를 계산
                if z < y:
                    continue  # z가 y보다 작으면 더 이상 검사할 필요가 없음
                if z in counter:
                    if x == y == z:  # 세 숫자가 모두 같은 경우
                        result += counter[x] * (counter[x] - 1) * (counter[x] - 2) // 6
                    elif x == y != z:  # 첫 번째와 두 번째가 같고 세 번째가 다른 경우
                        result += counter[x] * (counter[x] - 1) // 2 * counter[z]
                    elif x != y and y == z:  # 첫 번째가 다르고 두 번째와 세 번째가 같은 경우
                        result += counter[x] * counter[y] * (counter[y] - 1) // 2
                    elif x < y < z:  # 세 숫자가 모두 다른 경우
                        result += counter[x] * counter[y] * counter[z]

        return result % MOD
