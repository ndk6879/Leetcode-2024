class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_counts = {0: 1}
        odd_count = 0

        for num in nums:
            # 현재 숫자가 홀수면 홀수 개수 증가
            if num % 2 == 1:
                odd_count += 1
            
            # (odd_count - k)가 prefix_counts에 있으면 그 개수만큼 결과에 더함
            if odd_count - k in prefix_counts:
                count += prefix_counts[odd_count - k]
            
            # 현재까지의 odd_count를 prefix_counts에 추가
            if odd_count in prefix_counts:
                prefix_counts[odd_count] += 1
            else:
                prefix_counts[odd_count] = 1

        return count
