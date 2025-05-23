from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 1. 현재 배열에 이미 존재하는 K의 개수를 셈
        starting_frequency = nums.count(k)

        # 2. 연속 구간에서 바꿔서 만들 수 있는 최대 K 개수
        max_duplicates = 0

        # 3. 가능한 모든 target 값을 시도 (1부터 50까지)
        for target_value in range(1, 51):
            if target_value == k:
                continue  # 원래 K는 이미 포함했으니까 패스

            current_freq = 0  # 현재 구간에서 만들 수 있는 K 개수
            current_max = 0   # 그 중 최대값 저장

            for num in nums:
                if num == target_value:
                    current_freq += 1  # 이 숫자는 바꾸면 K가 됨
                elif num == k:
                    current_freq -= 1  # 이미 K인 숫자는 바꾸면 K가 사라짐

                # 누적합이 0보다 작으면 버리고 새로 시작
                current_freq = max(current_freq, 0)

                # 지금까지 가장 많이 만든 K 개수 저장
                current_max = max(current_max, current_freq)

            # 이 target_value로 만든 K 수 중 가장 많은 경우 저장
            max_duplicates = max(max_duplicates, current_max)

        # 최종 정답 = 기존 K + 새로 만든 K
        return max_duplicates + starting_frequency
